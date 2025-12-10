# Watsonx Agent Garden 🪴

Welcome to the Watsonx Agent Garden 🪴 - a collection of AI agents customized for real-world industry use cases. Each use case demonstrates practical applications of Watsonx agents solving specific business challenges.

## Overview

This repository showcases production-ready AI agents built with Watsonx, demonstrating how to leverage agentic AI for various industry verticals. Each use case includes complete implementations, documentation, and video walkthroughs.

## Available Use Cases

### Insurance Use Case
**AI-powered insurance agent with RAG, guidelines, and policy management**

A comprehensive insurance agent that handles policy inquiries, generates quotes, and manages policy submissions using agentic RAG, guidelines, and custom tools.

**Features:**
- Agentic RAG for knowledge retrieval from insurance fund rules
- Guidelines for structured responses to common inquiries
- Custom pricing tool for generating life insurance quotes
- Policy submission integration with Langflow and FastAPI

**Documentation:** See the [Insurance Use Case documentation](docs/insurance.md) for detailed walkthroughs and implementation guides.

## Repository Structure

```
AIForIndustry/
├── 1.Insurance/        # Insurance use case implementation
│   ├── api.py         # FastAPI server for policy submission
│   ├── quoting.py     # Life insurance quote tool
│   ├── policysubmission.py  # Policy submission logic
│   ├── requirements.txt     # Python dependencies
│   └── README.md      # Detailed setup instructions
├── 2.Banking/          # Banking use case (coming soon)
└── docs/              # Documentation site
    ├── index.md       # Main documentation page
    └── insurance.md   # Insurance use case documentation
```

## Getting Started

1. **Clone the repository**: 
   ```bash
   git clone <repository-url>
   cd AIForIndustry
   ```

2. **Install dependencies**:
   ```bash
   pip install uv
   uv sync
   ```

3. **Explore use cases**:
   - Start with the [Insurance Use Case](1.Insurance/README.md) for a complete example
   - Review the code and documentation in each use case folder
   - Follow along with the video walkthroughs in the [documentation site](https://nicknochnack.github.io/WatsonxAgentGarden)

## Prerequisites

Before you begin, make sure you have:
- Access to Watsonx services
- Python 3.11+ installed
- Git for cloning the repository
- Basic understanding of AI agents and Watsonx
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

## Documentation

For detailed documentation and video walkthroughs, visit the [documentation site](https://nicknochnack.github.io/WatsonxAgentGarden).

## Contributing

This repository contains industry-specific use cases for Watsonx agents. Each use case is designed to be self-contained with its own implementation, documentation, and examples.

## License

This project is licensed under the MIT License.

---

**Author**: Nick Renotte - AI Engineer and Content Creator  
**Version**: 1.x
