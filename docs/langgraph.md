---
layout: default
title: "Chapter 3: Langgraph"
nav_order: 4
description: "Pro-code agent development with Python and graph architectures"
---

# Chapter 3: Pro-Code Agent Development with Langgraph

Welcome to the most powerful chapter of our course! Here we dive into **pro-code agent development** using Langgraph - giving you complete control over sophisticated AI agent architectures.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117080100?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Intro-Langgraph"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## Learning Objectives

By the end of this chapter, you'll be able to:
- Understand Langgraph's graph-based agent architecture
- Build agents with persistent memory and conversation history
- Integrate external tools and APIs into your agents
- Create structured output agents with type safety
- Implement search and web scraping capabilities
- Build complex multi-agent workflows with state management

## What is Langgraph?

Langgraph is a library for building stateful, multi-actor applications with LLMs. Key features include:
- **Graph-based architecture** for complex agent workflows
- **Persistent state management** across conversations
- **Tool integration** for external system access
- **Multi-agent coordination** with shared state
- **Streaming support** for real-time interactions
- **Built-in persistence** for production deployments

## Setup Instructions

Before diving into the exercises, ensure your environment is ready:

```bash
# Navigate to the Langgraph directory
cd "3. Langgraph"

# Install dependencies (if not already done)
uv sync

# Set up your environment variables by updating .env_sample to .env and filling in these values 
WATSONX_APIKEY="<YOUR WATSONX API KEY HERE>"
WATSONX_PROJECT_ID="<YOUR WATSONX PROJECT ID HERE>"
MODEL_ID=meta-llama/llama-4-maverick-17b-128e-instruct-fp8
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

## Progressive Learning Path

### 0. Basic Agent (`0. basic.py`)

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117630624?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Langgraph1-Basic"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

**Objective**: Understand the fundamental Langgraph structure

**What you'll learn**:
- Basic agent setup and configuration
- Simple conversation flow
- State management basics

**Try this**:
```python
python "0. basic.py"
```

### 1. Memory Agent (`1. memory.py`)

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117630693?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Langgraph2-Memory"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

**Objective**: Add persistent memory to your agent

**What you'll learn**:
- Conversation history management
- State persistence across sessions
- Memory retrieval and context handling

**Test prompts**:
1. `"My name is Nick"`
2. Continue the conversation to test memory retention e.g. `"What's my name?"`

**Key concepts**:
- **Checkpointing**: Save conversation state
- **Memory retrieval**: Access previous context
- **State updates**: Modify conversation history

### 2. Tool Integration (`2. tool.py`)

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117630713?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Langgraph3-Tools"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

**Objective**: Connect your agent to external tools

**What you'll learn**:
- Tool definition and registration
- GitHub API integration
- Structured tool responses

**Test prompt**:
```
"Get me the trending Python repos on GitHub"
```

**Tools demonstrated**:
- GitHub repository search
- API response processing
- Error handling for external services

### 3. Structured Outputs (`3. structured.py`)

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117630760?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Langgraph4-Structured"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

**Objective**: Generate type-safe, structured responses

**What you'll learn**:
- Pydantic model integration
- Type safety for agent outputs
- Structured data validation

**Test prompt**:
```
"What are the trending Python repos on GitHub?"
```

**Key features**:
- **Type safety**: Ensure output conforms to expected structure
- **Validation**: Automatic data validation
- **Serialization**: Easy conversion to JSON/other formats

## Key Concepts

### Graph-Based Architecture

Langgraph uses a directed graph structure where:
- **Nodes** represent different agent functions
- **Edges** define the flow between functions
- **State** is passed and modified between nodes
- **Conditional routing** enables dynamic workflow paths

### State Management

```python
from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[str]
    user_input: str
    agent_response: str
    context: dict
```

### Tool Integration

```python
from langchain.tools import tool

@tool
def github_search(query: str) -> str:
    """Search GitHub repositories"""
    # Implementation here
    return results
```

### Memory and Persistence

- **Checkpointing**: Automatic state saving
- **Thread management**: Separate conversation threads
- **Retrieval**: Access historical context
- **State updates**: Modify conversation memory

## Advanced Features

### Multi-Agent Coordination
- **Agent communication**: Pass messages between agents
- **Shared state**: Common memory across agents
- **Role specialization**: Different agents for different tasks
- **Workflow orchestration**: Complex multi-step processes

### Streaming and Real-time
- **Response streaming**: Real-time output generation
- **Event handling**: React to user inputs immediately
- **Async processing**: Non-blocking operations
- **Progress tracking**: Monitor long-running tasks

### Production Deployment
- **API endpoints**: Deploy as REST APIs
- **Scaling**: Handle multiple concurrent users
- **Monitoring**: Track performance and usage
- **Error handling**: Robust error recovery

## Code Examples

### Basic Agent Structure
```python
from langgraph.graph import StateGraph
from langgraph.checkpoint.sqlite import SqliteSaver

# Define state
class State(TypedDict):
    messages: List[str]

# Create graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)

# Add edges
workflow.add_edge("agent", "tools")
workflow.add_edge("tools", "agent")

# Compile
app = workflow.compile(checkpointer=SqliteSaver("memory.db"))
```

### Tool Usage
```python
from langchain_core.tools import tool

@tool
def web_search(query: str) -> str:
    """Search the web for information"""
    # Implementation
    return search_results

tools = [web_search]
agent = create_agent(llm, tools)
```

## Practice Projects

### Project 1: Research Assistant
Build an agent that:
- Searches multiple sources
- Synthesizes information
- Maintains research context
- Generates reports

### Project 2: Code Review Agent
Create an agent that:
- Analyzes code repositories
- Identifies issues and improvements
- Suggests optimizations
- Tracks changes over time

### Project 3: Multi-Agent Customer Service
Develop a system with:
- Intake agent for initial questions
- Specialist agents for different domains
- Escalation protocols
- Shared customer context

## Debugging and Development

### Common Issues
1. **State management**: Ensure proper state updates
2. **Tool integration**: Verify tool function signatures
3. **Memory persistence**: Check checkpointing configuration
4. **Error handling**: Implement robust error recovery

### Development Tips
1. **Start simple**: Begin with basic functionality
2. **Test incrementally**: Add one feature at a time
3. **Monitor state**: Use logging to track state changes
4. **Use type hints**: Enable better IDE support and debugging

## Next Steps

Ready to deploy your agents responsibly? Move on to:

**[Chapter 4: Governance](governance)** - Learn AI governance, evaluation, and monitoring

---

## Related Files

Explore the Langgraph examples:
```
3. Langgraph/
├── 0. basic.py              # Basic agent structure
├── 1. memory.py             # Memory and persistence
├── 2. tool.py               # Tool integration
├── 3. structured.py         # Structured outputs
├── 4. search.py             # Web search capabilities
├── 5. endpointreview.py     # Endpoint analysis
├── requirements.txt         # Dependencies
└── README.md               # Setup instructions
```

## Additional Resources

- [Langgraph Documentation](https://langchain-ai.github.io/langgraph/) - Official documentation
- [Python SDK Reference](https://python.langchain.com/docs/langgraph) - API reference
- [Example Applications](https://github.com/langchain-ai/langgraph/tree/main/examples) - Community examples
- [Nicks Langgraph Crash Course](https://youtu.be/OojcSzWrjsg?si=4DoPvGp79GxobYyB) - Need a deeper dive, I've got a full crash course here. 