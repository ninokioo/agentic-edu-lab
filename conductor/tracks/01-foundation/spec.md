# Track 01: Foundation

## Objective
Establish the foundational infrastructure for the Local-First Ecosystem.

## Specifications
1. **LLM Node:** Ensure local access to Ollama (Gemma 3 / Qwen) on 10.10.10.80.
2. **Graph DB:** Initialize Gel (EdgeDB) on 10.10.10.140. Create schema SkillNode mapping user_id, skill_name, and proficiency.
3. **MCP Server:** Develop mcp-memory-server in Python (using FastMCP) to read and write states to the DB.
