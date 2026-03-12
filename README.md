# AI Agentic Systems: Educational Framework (Agentic Education Lab)

### Project Overview
An internal research repository dedicated to exploring multi-agent orchestration, automated code generation, and autonomous learning systems. This project is built by and for educational research purposes on **Arch Linux** and **EndeavourOS**.

### Strategic Direction: Local Exocortex Swarm
We are actively building an **R&D Agentic Autonomous Learning System** aimed at solving Benjamin Bloom's "2 Sigma Problem" through personalized, AI-driven pedagogy. 
Instead of a monolithic cloud LMS, we utilize a **Local-First Exocortex** architecture:
- **Graph Memory:** Tracking user cognitive states (Skill Nodes) using **GelDB** (EdgeDB).
- **Local Inference:** Running routine routing and orchestration via **Ollama** (Gemma 3 / Qwen).
- **Deep Pedagogy:** Socratic tutoring and complex evaluation handled by frontier models (Claude 3.5 Sonnet).
- **Integration:** All components communicate securely via the **Model Context Protocol (MCP)**.

👉 *See the full strategic implementation plan in [conductor/agentic-edu-rd-plan.md](conductor/agentic-edu-rd-plan.md).*

### Core Objectives
- **LLM Benchmarking:** Evaluating Claude 3.5/4.6 Sonnet performance in Socratic agentic workflows.
- **MCP Development:** Building specialized `mcp-memory-server` and evaluator tools for local environments.
- **Automated Refactoring & Review:** Testing autonomous agents for code modernization and educational code review.

### Research Scope
- **Industry:** Education / AI Literacy
- **Target Audience:** Internal developers and AI researchers.
- **Key Models:** Anthropic Claude (via Vertex AI), Gemini Pro, local models via Ollama.

---
*This repository serves as the official documentation and deployment source for the internal web portal.*