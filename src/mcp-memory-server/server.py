#!/usr/bin/env python3
"""
MCP Memory Server for Agentic Education Lab.
Handles state persistence and Knowledge Graph interactions via GelDB (EdgeDB).
"""

from mcp.server.fastmcp import FastMCP
import edgedb
import json

# Initialize the FastMCP server
mcp = FastMCP("AgenticEduMemoryServer")

# In the future, this will connect to the GelDB instance on 10.10.10.140:5656
# client = edgedb.create_client()

@mcp.tool()
def add_skill_node(user_id: str, skill_name: str, proficiency: int) -> str:
    """
    Records or updates a user's proficiency level in a specific skill.
    This acts as the fundamental node in the learner's Knowledge Graph.
    
    Args:
        user_id: Unique identifier for the student.
        skill_name: The concept or skill being learned (e.g., 'Rust Ownership').
        proficiency: An integer score (e.g., 0-100) representing mastery.
    """
    # TODO: Implement actual EdgeDB/Gel insertion logic here
    # Example EdgeQL: 
    # INSERT SkillNode { user_id := <user_id>, name := <skill_name>, level := <proficiency> }
    
    print(f"[DEBUG] Adding skill '{skill_name}' (Level: {proficiency}) for user '{user_id}'.")
    return json.dumps({
        "status": "success",
        "action": "add_skill_node",
        "data": {
            "user_id": user_id,
            "skill": skill_name,
            "level": proficiency
        }
    })

@mcp.tool()
def get_user_skills(user_id: str) -> str:
    """
    Retrieves the entire cognitive state (all skill nodes) for a specific user.
    Used by the Orchestrator to determine the next curriculum step.
    
    Args:
        user_id: Unique identifier for the student.
    """
    # TODO: Implement actual EdgeDB/Gel query logic here
    # Example EdgeQL:
    # SELECT SkillNode { name, level } FILTER .user_id = <user_id>
    
    print(f"[DEBUG] Retrieving skills for user '{user_id}'.")
    # Returning mock data for initial testing
    mock_data = [
        {"skill": "Basic Python", "level": 90},
        {"skill": "Rust Ownership", "level": 20},
    ]
    
    return json.dumps({
        "status": "success",
        "user_id": user_id,
        "skills": mock_data
    })

if __name__ == "__main__":
    print("Starting AgenticEduMemoryServer via standard input/output...")
    # FastMCP uses standard IO for MCP communication by default
    mcp.run()
