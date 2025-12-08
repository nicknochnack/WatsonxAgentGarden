from typing import Annotated, List
from langgraph.graph import START,END, StateGraph
from langgraph.graph.message import add_messages 
from langchain_ibm import ChatWatsonx 
from langgraph.prebuilt import ToolNode
from pydantic import BaseModel, Field
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv 
import os 
from colorama import Fore 
from src.tools.github import trending
import json

load_dotenv() 

class GitHubRepo(BaseModel): 
    repoName: str = Field(description="What is the name of the repo")  
    stars: int = Field(description="How many stars does it have?")  

class GitHubRepos(BaseModel):
    repositories: List[GitHubRepo] = Field(description="List of GitHub repositories")
    total_count: int = Field(description="Total number of repositories found")

llm = ChatWatsonx(
    model_id="meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
    project_id=os.environ['WATSONX_PROJECT_ID'],
    params={'max_tokens':5000}
)
tools = [trending]
tool_node = ToolNode(tools) 

llmwithtools = llm.bind_tools(tools)
llmwithstructure = llm.with_structured_output(GitHubRepos)

def structured_output_template(response:str) -> str: 
   return f"""You are an assistant designed to assist with analysing github projects.
    Return the repo name and stars as a json object. 

    {response}
    """

class State(dict): 
    messages: Annotated[list, add_messages]

def chatbot(state:State): 
    return {'messages':[llmwithtools.invoke(state['messages'])]}

def outputparser(state:State): 
    last_message = state['messages'][-1]
    res = llmwithstructure.invoke(structured_output_template(last_message.content))
    return {'messages': json.dumps(res.model_dump(), indent=2)}

def router(state:State):
    last_message = state['messages'][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls: 
        return "tools" 
    else: 
        return "output"


graph_builder = StateGraph(State) 
graph_builder.add_node("chatbot", chatbot) 
graph_builder.add_node("tools", tool_node) 
graph_builder.add_node("output", outputparser) 
graph_builder.add_edge(START, "chatbot") 
graph_builder.add_edge("tools", "chatbot") 
graph_builder.add_edge("output", END) 
graph_builder.add_conditional_edges("chatbot", router) 
memory = InMemorySaver()
graph = graph_builder.compile(checkpointer=memory) 


if __name__ == '__main__': 
    while True: 
        prompt = input(Fore.LIGHTCYAN_EX + "⚡️ Enter your prompt here: " + Fore.RESET)
        # Use proper message format
        result = graph.invoke(
            {"messages": [
                {'role':'system', 'content':'You are a helpful assistant designed to assist with user queries'}, 
                {'role':'user', 'content':prompt}
                ]},  
            config={"configurable": {"thread_id": 1234}}
        ) 
        print(Fore.LIGHTMAGENTA_EX + result['messages'][-1].content + Fore.RESET) 