# Add this buddy: https://github.com/IBM/ibm-watsonx-gov/blob/samples/notebooks/python_sdk/agentic/Evaluation%20of%20Tool%20Calls%20in%20LangGraph%20Agent.ipynb
# Documentation: https://ibm.github.io/ibm-watsonx-gov/setup_wx_gov_as_service.html 

from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.tools import tool
from langgraph.prebuilt import ToolNode
from ibm_watsonx_gov.evaluators.agentic_evaluator import AgenticEvaluator
from ibm_watsonx_gov.config import AgenticAIConfiguration

import uuid 
import json
from colorama import Fore 
from enum import Enum
from langchain_ibm import ChatWatsonx 
from langgraph.checkpoint.memory import MemorySaver
import os 
from dotenv import load_dotenv 
import yfinance as yf

load_dotenv()

class StockTickers(str, Enum):
    amazon = "AMZN"
    ibm = "IBM"
    nvidia = "NVDA"

# Build tool
@tool
def get_stock_price(stock_ticker: StockTickers) -> str:
    """Returns the last stock price for a given stock.

    Args:
         stock_ticker: A stock ticker accepted on yahoo finance.

    Returns:
         The last stock price in USD."""
    
    ticker = yf.Ticker(stock_ticker)
    prices = ticker.history(period="1mo")
    price = prices["Close"].iloc[-1]
    return f"The current stock price for {stock_ticker} is {price}"

#  Define state consistent with structured.py
class State(dict):
    messages: Annotated[list, add_messages]
    interaction_id: str
    input_text: str
    generated_text: str
    tool_calls: str
    record_id: str

# Setup LLM and tools
llm = ChatWatsonx(
    model_id="meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
    project_id=os.environ['WATSONX_PROJECT_ID'],
    params={'max_tokens': 5000, 'decoding_method': 'greedy'}
)

tools = [get_stock_price]
tool_node = ToolNode(tools)
llm_with_tools = llm.bind_tools(tools)

# Setup evaluator
evaluator = AgenticEvaluator()

@evaluator.evaluate_tool_call_syntactic_accuracy(configuration=AgenticAIConfiguration(tools=tools), compute_real_time=False)
def chatbot(state: State):
    response = llm_with_tools.invoke(state['messages'])
    print(Fore.LIGHTYELLOW_EX + str(response) + Fore.RESET)  
    return {"input_text":state["messages"][0], "messages": [response], "generated_text":response, "tool_calls": response.tool_calls}


# Router function consistent with structured.py pattern
def router(state: State):
    last_message = state['messages'][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls: 
        return "tools" 
    else: 
        return END

# Build graph consistent with structured.py
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_conditional_edges("chatbot", router)

# Compile graph
# memory = MemorySaver()
graph = graph_builder.compile() #checkpointer=memory)

if __name__ == '__main__':
    config = {"configurable": {"thread_id": "abc123"}}
    
    while True:
        prompt = input(Fore.LIGHTCYAN_EX + "⚡️ Enter your prompt here: " + Fore.RESET)
        if prompt.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        
        evaluator.start_run()
        
        # Use proper message format consistent with structured.py
        result = graph.invoke(
            {"messages": [
                {'role': 'system', 'content': 'You are a helpful assistant designed to assist with stock queries'}, 
                {'role': 'user', 'content': prompt}
            ],"interaction_id":str(uuid.uuid1()), "record_id":str(uuid.uuid1())},
            config=config
        )
        
        print(Fore.LIGHTMAGENTA_EX + result['messages'][-1].content + Fore.RESET)
        
        evaluator.end_run()
        
        # Save evaluation results
        eval_result = evaluator.get_result() 
        with open('trace.json', 'w') as f: 
            json.dump(eval_result.get_aggregated_metrics_results(), f) 