---
title: "Chapter 2: Langflow"
layout: default
nav_order: 3
description: "Visual agent development with low-code workflows"
---

# Chapter 2: Visual Agent Development with Langflow

Welcome to Chapter 2! Here we'll explore **low-code visual agent development** using Langflow - the perfect middle ground between no-code simplicity and full programming control.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117079707?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Intro-Langflow"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## Learning Objectives

By the end of this chapter, you'll be able to:
- Set up and navigate the Langflow visual interface
- Build basic chatbots using IBM watsonx.ai models
- Create agentic workflows with tool integration
- Implement post-processing with advanced prompt engineering
- Deploy and test your visual agent workflows

## What is Langflow?

Langflow is a visual framework for building multi-agent and RAG applications. It provides:
- **Drag-and-drop interface** for creating AI workflows
- **Pre-built components** for common AI tasks
- **Visual debugging** to see data flow between components
- **Easy deployment** of your completed workflows
- **Integration** with multiple LLM providers and vector databases

## Setup Instructions

Getting started with Langflow is straightforward:

### Option 1: DataStax Trial (Recommended)

1. **Sign up for a Langflow Trial via the DataStax Website**:
   ```
   https://astra.datastax.com/signup?type=langflow
   ```

2. **Access Langflow**:
   ```
   https://astra.datastax.com/langflow
   ```

3. **Start building** your first flow!

### Option 2: Local Installation

If you prefer to run Langflow locally:

```bash
pip install langflow
langflow run
```

Then open your browser to `http://localhost:7860`

## Course Exercises

### Exercise A: Basic Prompting

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117305073?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Langflow1-Basic"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

First up, we'll create a simple chatbot with no tools - this establishes the groundwork for more complex agents.

![Exercise A - Basic Prompting Workflow](https://i.imgur.com/DBlvM6A.png)
*Basic prompting workflow showing Chat Input → IBM watsonx.ai → Chat Output*

**System Prompt**:
```
You are a helpful agent designed to assist with user queries.
```

**Nodes Required**:
- **Chat Input** - Receives user messages
- **IBM watsonx.ai** - Language model for processing
- **Chat Output** - Displays agent responses

**Workflow Setup**:
1. Add a Chat Input component
2. Connect it to IBM watsonx.ai component
3. Configure the system prompt in the watsonx.ai component
4. Connect to Chat Output component

**Test Prompts**:
- "How do LLMs work?"
- "Why is trust in AI important?"
- "How can we detect hallucination?"

### Exercise B: Creating an Agent with Tool Nodes

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117304558?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Langflow2-Arxiv"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

Now we enhance our basic chatbot by converting it into an agent with tool access. We'll add the Arxiv tool for researching the latest research papers.

![Exercise B - Agent with Tools](https://i.imgur.com/xRJe30m.png)
*Enhanced workflow with Agent node orchestrating IBM watsonx.ai and Arxiv tool*

**Additional Nodes Required**:
- **Arxiv** - Tool for academic paper research
- **Agent** - Orchestrates tool usage and responses

**Workflow Enhancement**:
1. Replace the direct IBM watsonx.ai connection with an Agent node
2. Connect the Arxiv tool to the Agent
3. Configure the Agent to use IBM watsonx.ai as the underlying model
4. Test the enhanced workflow

**Test Prompts**:
- "What are the trending papers in machine learning governance?"
- "Is there any new research on LLM hallucinations?"
- "Find recent papers about AI safety and alignment"

### Exercise C: Post Processing with Prompt Engineering

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117303705?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Langflow3-PostProc"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

This exercise demonstrates sophisticated prompt engineering for post-processing and integrating web scraping capabilities.


![Exercise C - Multi Tool Setup](https://i.imgur.com/UkLWEDP.png)
*Multi-tool workflow with Arxiv, Agent, FirecrawlScrapeAPI, and post-processing*


![Exercise C - Output Parsing](https://i.imgur.com/5DLyYqI.png)
*Output parsing and evaluation workflow with Prompt component for quality assessment*

**Engineered Prompt**:
```
Review the following input and rate the output on a scale of 1-10 on how much clarity it provides.
{chat_input}
```

**Additional Nodes Required**:
- **FirecrawlScrapeAPI** - Set to tool node for web scraping
- **Prompt** - For advanced prompt engineering and post-processing

**Workflow Enhancement**:
1. Add FirecrawlScrapeAPI as a tool node
2. Connect it to your existing agent
3. Add a Prompt component for post-processing evaluation
4. Configure the evaluation prompt template

**Test Prompt**:
```
Summarise this page - https://www.ato.gov.au/about-ato/commitments-and-reporting/information-and-privacy/ato-ai-transparency-statement
```

## Key Concepts

### Visual Programming Progression

#### Level 1: Basic Prompting
- **Simple chat flow**: Input → LLM → Output
- **System prompts**: Define agent behavior
- **Direct responses**: No external tool access

#### Level 2: Agentic Behavior
- **Tool integration**: Access to external resources
- **Decision making**: Agent chooses when to use tools
- **Research capabilities**: Can gather current information

#### Level 3: Advanced Processing
- **Post-processing**: Evaluate and refine outputs
- **Web scraping**: Access live web content
- **Quality assessment**: Rate and improve responses

### Component Deep Dive

#### Core Components
- **Chat Input/Output**: User interface components
- **IBM watsonx.ai**: Enterprise-grade language model
- **Agent**: Orchestrates multiple tools and decisions
- **Prompt**: Advanced prompt engineering and templating

#### Tool Components
- **Arxiv**: Academic research paper search
- **FirecrawlScrapeAPI**: Web content extraction
- **Custom Tools**: Extensible for specific needs

#### Processing Components
- **Memory**: Conversation context management
- **Evaluators**: Quality assessment and scoring
- **Filters**: Content processing and refinement

### Low-Code Benefits

- **Faster development**: Visual interface speeds up creation
- **Better collaboration**: Non-technical team members can contribute
- **Easier debugging**: Visual flow makes issues obvious
- **Rapid prototyping**: Quick iteration and testing
- **Enterprise integration**: Native support for IBM watsonx.ai

## Advanced Workflows

### Multi-Tool Research Agent
Combine multiple tools for comprehensive research:
1. **Arxiv** for academic papers
2. **FirecrawlScrapeAPI** for web content
3. **Agent** orchestrates tool selection
4. **Post-processing** evaluates and synthesizes results

### Quality Assessment Pipeline
Implement automated quality control:
1. **Initial response** generation
2. **Clarity evaluation** using prompt engineering
3. **Iterative improvement** based on scores
4. **Final output** with quality metrics

## Practice Projects

### Project 1: Academic Research Assistant
Build an agent that:
- Searches academic papers via Arxiv
- Scrapes relevant web content
- Synthesizes findings with clarity scoring
- Provides comprehensive research summaries

### Project 2: Government Policy Analyzer
Create a workflow that:
- Scrapes government policy documents
- Evaluates content clarity and accessibility
- Provides simplified summaries
- Rates information quality

### Project 3: AI Governance Monitor
Develop an agent for:
- Tracking AI policy developments
- Analyzing transparency statements
- Monitoring research trends
- Providing governance insights

## Debugging and Optimization

### Visual Debugging
1. **Component inspection**: Check data flow between nodes
2. **Message tracing**: Follow conversation paths
3. **Tool monitoring**: Verify tool calls and responses
4. **Performance metrics**: Monitor response times and quality

### Common Issues
- **Tool connectivity**: Ensure API keys are properly configured
- **Prompt formatting**: Check template syntax and variables
- **Agent routing**: Verify tool selection logic
- **Output formatting**: Ensure consistent response structure

## Next Steps

Ready to take your skills to the next level with full programming control? Move on to:

**[Chapter 3: Langgraph](langgraph)** - Master pro-code agent development with Python

---

## Related Files

Explore the Langflow resources:
```
2. Langflow/
├── README.md                      # Setup instructions
└── Screenshot 2025-09-03...png    # Interface example
```

## Additional Resources

- [Langflow Documentation](https://docs.langflow.org/) - Official documentation
- [Community Flows](https://github.com/langflow-ai/langflow) - Example workflows from the community
- [DataStax Langflow](https://astra.datastax.com/langflow) - Hosted Langflow service
- [IBM watsonx.ai Integration](https://www.ibm.com/products/watsonx-ai) - Enterprise AI platform