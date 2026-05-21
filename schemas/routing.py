from typing import List
from pydantic import BaseModel, Field

class SubTask(BaseModel):
    agent_type: str = Field(description="The specialized agent to route to: 'search', 'summarize', or 'validate'")
    instruction: str = Field(description="Specific instruction for this sub-agent")
    depends_on: List[int] = Field(default=[], description="List of previous step indices this step depends on")

class ExecutionPlan(BaseModel):
    plan: List[SubTask] = Field(description="The sequential list of subtasks to execute")
