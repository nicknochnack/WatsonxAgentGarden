---
title: "Chapter 1: Orchestrate"
nav_order: 2
description: "Building no-code AI agents with Watsonx Orchestrate"
---

# Chapter 1: Building Agents with Watsonx Orchestrate

Welcome to the first chapter of our Watsonx Agentic AI course! This section introduces you to **no-code agent building** using Watsonx Orchestrate - perfect for business users and those new to AI agent development.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117081743?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Intro-Orchestrate"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## Learning Objectives

By the end of this chapter, you'll be able to:
- Understand what Watsonx Orchestrate is and how it works
- Build agents without writing any code
- Integrate tools and knowledge bases into your agents
- Create agentic RAG (Retrieval Augmented Generation) solutions
- Use external tools like Firecrawl for web scraping

## What is Watsonx Orchestrate?

Watsonx Orchestrate is IBM's no-code platform for building AI-powered agents and automating business processes. It allows you to:
- Create conversational AI agents without programming
- Connect to various data sources and APIs
- Build complex workflows using a visual interface
- Deploy agents that can understand natural language and perform tasks

## Setup Instructions

Before we begin, you'll need to set up your environment:

## Course Exercises

### Exercise A: Basic Agent Interactions

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117273003?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Orchestrate1-Basic"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

Start with these fundamental questions to understand your agent's capabilities:

1. **"What is the 7 layer OSI model?"**
   - This tests the agent's knowledge of networking fundamentals
   - Observe how the agent structures its response

2. **"What is typical useful life for a CRM system like Siebel?"**
   - Tests business domain knowledge
   - Notice the agent's understanding of enterprise software

3. **"How should I evaluate ICT investment decisions over the short, medium and long term?"**
   - Complex business strategy question
   - Shows the agent's ability to provide structured advice

### Exercise B: Adding Agentic RAG

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117273043?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Orchestrate2-RAG"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

Now we'll enhance our agent with domain-specific knowledge:

**Knowledge Base Description:**
> This knowledge covers DTA's digital service standard, which establishes the requirements for designing and delivering digital government services. The Standard puts people and business at the centre of government digital service delivery. It guides digital teams to create and maintain digital services that are user-friendly, inclusive, adaptable and measurable.

**Try these prompts after adding the knowledge base:**
- "What are the key principles of the digital service standard?"
- "How should we design user-friendly government services?"
- "What makes a digital service inclusive and accessible?"

### Exercise C: External Tool Integration

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1117273380?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Orchestrate3-MCP"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

Learn to integrate external tools for real-time data access:

1. **Set up Firecrawl tool**:
   ```bash
   env FIRECRAWL_API_KEY=your_api_key_here npx -y firecrawl-mcp
   ```

2. **Add the tool**: `Firecrawl:firecrawl_scrape`

3. **Test with this prompt**:
   ```
   Extract the opportunities from https://www.buyict.gov.au/sp?id=opportunities
   ```

This exercise demonstrates how agents can interact with live web data to provide current information.

## Essential Resources

- [Getting Started Tutorial](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=getting-started-watsonx-orchestrate) - Official IBM documentation
- [Agent Development Kit (ADK)](https://developer.watson-orchestrate.ibm.com/) - Deep dive into advanced development features

## Key Concepts

### No-Code Development
- **Visual Interface**: Build agents using drag-and-drop components
- **Natural Language**: Configure agents using plain English descriptions
- **Pre-built Integrations**: Connect to popular business applications without coding

### Agentic RAG
- **Knowledge Integration**: Add custom knowledge bases to your agents
- **Context-Aware Responses**: Agents provide answers based on your specific documents
- **Dynamic Learning**: Agents can access and reason over your organizational knowledge

### Tool Integration
- **External APIs**: Connect to web services and databases
- **Real-time Data**: Access current information from live sources
- **Workflow Automation**: Chain multiple tools together for complex tasks

## Practice Exercises

1. **Create Your First Agent**:
   - Build a simple Q&A agent for your organization
   - Test it with domain-specific questions

2. **Add Knowledge Sources**:
   - Upload relevant documents to create a knowledge base
   - Test how the agent uses this information

3. **Integrate External Tools**:
   - Connect to a web API or database
   - Create workflows that combine multiple data sources

## Next Steps

Once you've mastered no-code agent building with Orchestrate, you're ready to move on to:

**[Chapter 2: Langflow](langflow)** - Learn visual, low-code agent development

---

## Related Files

All the code and resources for this chapter can be found in:
```
1. Orchestrate/
├── README.md                    # Original documentation
└── Digital Service Standard.pdf # Knowledge base document
```