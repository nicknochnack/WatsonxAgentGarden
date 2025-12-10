---
title: "Insurance Use Case"
layout: default
nav_order: 1
description: "AI-powered insurance agent with RAG, guidelines, and policy management"
---

# Insurance Use Case

This use case demonstrates a comprehensive AI-powered insurance agent built with Watsonx that handles policy inquiries, generates quotes, and manages policy submissions. The agent combines agentic RAG for knowledge retrieval, guidelines for structured responses, and custom tools for quote generation and policy submission.

## Overview

The insurance agent provides:
- **Agentic RAG**: Answers questions about insurance fund rules and policies
- **Guidelines**: Structured responses for common inquiries (e.g., direct debit information)
- **Pricing Tool**: Generates life insurance quotes based on customer information
- **Submission Tool**: Handles policy submissions via Langflow and FastAPI integration

## Video Walkthroughs

### 1. Introduction

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1145073306?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Insurance - Introduction"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

This introduction video provides an overview of the insurance use case, demonstrating how to build a comprehensive AI-powered insurance agent using Watsonx.

### 2. Agentic RAG

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1145073285?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Insurance - Agentic RAG"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Implementation Guide: Agentic RAG

Add knowledge retrieval capabilities to your agent:

1. **Select "Add Knowledge Source"** in Watsonx Orchestrate
2. **Choose "Other Sources"** and upload your PDF document
3. **Add the knowledge source description**:
   > This knowledge covers AIA Fund Rules. These Rules set out:
   > 1. the requirements for all Members;
   > 2. the rules regarding payment of Benefits by AIA Health Insurance Pty Ltd;
   > 3. the ways in which AIA Health Insurance Pty Ltd will conduct the Fund and make decisions regarding all Members; and
   > 4. all Members are bound by these Rules as amended from time to time.

4. **Test with sample prompts**:
   - "Summarise the fund rules for AIA"
   - "Explain it to me like I'm 5"
   - "Can I suspend my membership?"

**RAG Source**: [AIA Fund Rules](https://www.aia.com.au/en/help-and-support/forms-docs#tabfilter-05e20a84e2-item-5412a97eff-tab)

### 3. Guidelines

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1145073199?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Insurance - Guidelines"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Implementation Guide: Guidelines

Add structured response guidelines for common inquiries:

1. **Select "Add Guidelines"** in Watsonx Orchestrate
2. **Configure the guideline**:

   **Name**: `Direct Debit`
   
   **Condition**: 
   > If the customer requests information around direct debit details then do not provide an answer advise the customer to fill in the docusign form below.
   
   **Action**:
   > In order to change your Direct Debit details, all you have to do is fill out the Secure Docusign form below: https://powerforms.docusign.net/068e49e0-9e97-4783-b75d-793c9c5fd350?env=au&acct=f5702cdf-a901-446f-bbb8-31046047d20d&accountId=f5702cdf-a901-446f-bbb8-31046047d20d

3. **Test with prompt**: "Can you give me direct debit details"

### 4. Pricing Tool

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1145073260?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Insurance - Pricing Tool"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Implementation Guide: Pricing Tool

Integrate a custom Python tool for generating insurance quotes:

1. **Import the Python tool**:
   ```bash
   uv run orchestrate tools import -f quoting.py -r requirements.txt -k python
   ```

2. **Add the tool to your agent**:
   - Select "Add tool" > "Add from local instance" > `life_insurance_quote`

3. **Test with prompts**:
   - "Give me a life insurance quote"
   - The agent will prompt for: age, smoking habits, drinking habits, and heart problems history

### 5. Submission Tool

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1145073225?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Insurance - Submission Tool"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Implementation Guide: Policy Submission with Langflow x FastAPI

Integrate Langflow workflow with FastAPI for policy submissions:

1. **Start the FastAPI server**:
   ```bash
   uv run fastapi run 1.Insurance/api.py --port 8018
   ```

2. **Add custom component** into Langflow Desktop flow

3. **Update Langflow Flow description**:
   > A specialist insurance premium agent, capable of handling new policy creation, quotes and requests requiring insurance back end work.

4. **Add MCP server to Watsonx Orchestrate**:
   ```bash
   uvx mcp proxy http://host.docker.internal:7860/api/v1/mcp/project/<your-uuid-here>/sse
   ```

5. **Add the Insurance flow** to your agent

6. **Test with prompts**:
   - "Submit the policy quote from above"
   - "Submit this quote Name: Nick Renotte, DOB: 01012001, Quote Price: $300"

## Key Features

### Agentic RAG
- **Knowledge Base Integration**: Upload and query insurance fund rules and policies
- **Context-Aware Responses**: Agent retrieves relevant information from knowledge base
- **Natural Language Queries**: Ask questions in plain English

### Guidelines
- **Conditional Responses**: Trigger specific actions based on user queries
- **Structured Workflows**: Guide users to appropriate forms or resources
- **Consistent Messaging**: Ensure uniform responses for common inquiries

### Custom Tools
- **Quote Generation**: Calculate insurance quotes based on customer profile
- **Policy Management**: Handle policy creation and submission
- **API Integration**: Connect with backend systems via FastAPI

## Files and Resources

```
1.Insurance/
├── api.py                    # FastAPI server for policy submission
├── quoting.py                # Life insurance quote tool
├── policysubmission.py       # Policy submission logic
├── requirements.txt          # Python dependencies
└── README.md                 # Detailed setup instructions
```

## Additional Resources

- [Watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base)
- [Langflow Documentation](https://docs.langflow.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## Related Files

All implementation files for this use case can be found in:
```
1.Insurance/
├── api.py
├── quoting.py
├── policysubmission.py
├── requirements.txt
└── README.md
```

