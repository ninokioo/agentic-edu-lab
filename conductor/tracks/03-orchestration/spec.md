# Track 03: Orchestration Loop

## Objective
Implement the main Orchestrator that routes state between agents.

## Specifications
1. **LangGraph Setup:** Build the state machine connecting Orchestrator -> Curator -> Tutor -> Evaluator.
2. **Curriculum Generation:** Based on a target goal, generate a graph path of required sub-skills.
3. **Dynamic Routing:** If Evaluator fails the user artifact, route back to Tutor with specific context on the failure.
