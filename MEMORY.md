# Project Memory

## Purpose
This project is an automated Content Generation Pipeline designed to create written content (like blog posts) based on Product Requirements Documents (PRDs). The current example is a Beginner Sourdough Blog.

## Pipeline Stages
The pipeline is designed to be highly modular so that individual developers or AI agents can work on each component in parallel without interfering with each other.
1. **Researcher:** Reads the PRD and performs external searches (SerpApi) to find relevant sources.
2. **Outliner:** Takes research sources and organizes them into a structured outline.
3. **Drafter:** Expands the outline into a full draft using language models.
4. **Reviewer:** Reviews the final draft for tone, goals, and accuracy against the PRD.

## Architecture and Directory Structure
```
.
├── data/
│   ├── prd_example.md        # Example Product Requirements Document
│   └── sources.json          # Output of Researcher agent (and future intermediate artifacts)
├── scripts/
│   ├── adapters/             # External API adapters (SerpApi, OpenAI)
│   ├── agents/               # Individual pipeline stage agents
│   │   ├── researcher.py
│   │   ├── outliner.py
│   │   ├── drafter.py
│   │   └── reviewer.py
│   ├── mocks/                # Mock implementations of external services for testing
│   ├── utils.py              # Shared utility functions (json I/O, env variables)
│   ├── run_researcher.py     # Runner script for researcher
│   ├── run_outliner.py       # Runner script for outliner
│   ├── run_drafter.py        # Runner script for drafter
│   └── run_reviewer.py       # Runner script for reviewer
└── test/                     # Unit and integration tests
```

## Tech Stack
- **Language:** Python 3
- **LLM/Embeddings:** OpenAI (Currently heavily mocked in `scripts/mocks/mock_openai.py`)
- **Search:** SerpApi (Mocked via `scripts/mocks/mock_serpapi.py`)
- **Environment:** Mocking toggled via `USE_MOCKS` environment variable (`true` by default).

## State
Currently, the pipeline contains the Researcher agent, Outliner agent, Drafter agent, and Reviewer agent. Runner scripts exist for each step. Each agent reads from standard input JSON/Markdown files and outputs to standard JSON/Markdown files to decouple the stages.