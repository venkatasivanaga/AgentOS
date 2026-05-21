import pytest
from schemas.routing import ExecutionPlan, SubTask

def test_subtask_schema_validation():
    task = SubTask(
        agent_type="search",
        instruction="Find competitors",
        depends_on=[]
    )
    assert task.agent_type == "search"
    assert task.depends_on == []

def test_execution_plan_validation():
    plan = ExecutionPlan(plan=[
        SubTask(agent_type="search", instruction="step 1"),
        SubTask(agent_type="summarize", instruction="step 2", depends_on=[0])
    ])
    assert len(plan.plan) == 2
    assert plan.plan[1].depends_on == [0]
