from typing import Annotated
from langgraph.graph import START,END, StateGraph
from langgraph.graph.message import add_messages 
from langchain_ibm import ChatWatsonx 
from dotenv import load_dotenv 
import os 
from colorama import Fore 

load_dotenv() 

llm = ChatWatsonx(
    model_id="meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
    project_id=os.environ['WATSONX_PROJECT_ID'],
    params={'max_tokens':5000}
)

class State(dict): 
    messages: Annotated[list, add_messages]

def chatbot(state:State): 
    # print(Fore.LIGHTRED_EX + str(state) + Fore.RESET) 
    return {'messages':[llm.invoke(state['messages'])]}

graph_builder = StateGraph(State) 
graph_builder.add_node('chatbot', chatbot)
graph_builder.add_edge(START, 'chatbot')
graph_builder.add_edge('chatbot', END)
graph = graph_builder.compile() 

if __name__ == '__main__': 
    while True: 
        prompt = input(Fore.LIGHTCYAN_EX + "⚡️ Enter your prompt here: " + Fore.RESET)    
        result = graph.invoke(
            {"messages": [
                {'role':'system', 'content':'You are a helpful assistant designed to assist with user queries'}, 
                {'role':'user', 'content':prompt}
                ]}, 
            config={"configurable": {"thread_id": 1234}}
        ) 
        print(Fore.LIGHTMAGENTA_EX + result['messages'][-1].content + Fore.RESET) 