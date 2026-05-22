# Agent Instructions and Guidelines

## Welcome
If you are an AI agent or developer assigned to work on this repository, please read these guidelines carefully. This project is a modular pipeline for automated content generation based on PRDs.

## Goals & Philosophy
- **Modularity:** The project is cut into multiple stages (Research, Outline, Draft, Review). Each stage is completely decoupled. They communicate strictly through intermediate files (JSON/Markdown) saved in the `data/` directory.
- **Parallel Development:** Because each stage is isolated, multiple agents can be assigned to develop, optimize, or test different stages simultaneously. Always respect interface boundaries.
- **Token Efficiency:** Refer to `MEMORY.md` instead of exploring the whole codebase to understand the overarching structure.

## Tech Stack
- Python 3
- Gemini API (via `scripts/adapters/gemini_adapter.py`)
- DuckDuckGo Search (via `scripts/adapters/ddg_adapter.py`)

## Development Rules
2. **Decoupled Runners:** Every agent stage must have its own standalone runner script in `scripts/` (e.g., `run_outliner.py`). Never directly call one agent from another unless explicitly tasked to build a combined orchestrator.
3. **Artifact Standards:**
   - Input/Output paths should be configurable via CLI arguments (using `argparse`).
   - Default outputs should go into `data/`.
4. **Testing:** Write tests for your specific agent in `test/`. Because the agents are decoupled, you can easily mock the input artifact and verify the output artifact.

## Pipeline Breakdown
1. **Researcher:** PRD (`data/prd.md`) -> Sources (`data/sources.json`)
2. **Outliner:** Sources + PRD -> Outline (`data/outline.json`)
3. **Drafter:** Outline -> Draft (`data/draft.md`)
4. **Reviewer:** Draft + PRD -> Reviewed Draft (`data/reviewed_draft.md`)
