# Track 02: Agent Assembly

## Objective
Build specialized sub-agents that interface with the foundational memory.

## Specifications
1. **Socratic Tutor Agent:** System prompt engineering. Must never provide direct answers. Must ask guided questions. Connects to mcp-memory-server to adjust difficulty.
2. **Evaluator Agent:** Code analysis tool. Receives user artifacts and compares against required Skill Node criteria.
3. **Curator Agent:** Retrieves contextual documents (e.g., from local vector DB or web) to assist the Tutor.
