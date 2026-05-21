import json
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from schemas.routing import ExecutionPlan

class SupervisorAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
        self.structured_llm = self.llm.with_structured_output(ExecutionPlan)
        self.system_prompt = """You are the Supervisor Agent of AgentOS. 
        Break down complex user requests into smaller subtasks using these agents:
        1. 'search': For finding factual information.
        2. 'summarize': For condensing text.
        3. 'validate': For fact-checking.
        Return a logical execution plan."""

    def decompose_task(self, user_input: str) -> dict:
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{input}")
        ])
        chain = prompt | self.structured_llm
        result = chain.invoke({"input": user_input})
        return result.model_dump()
