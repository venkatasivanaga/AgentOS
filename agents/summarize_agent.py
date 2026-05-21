from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class SalesforceSummarizeAgent:
    """Transforms raw Salesforce JSON payloads into formatted executive briefings."""
    
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0.2)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an executive assistant inside Salesforce. Summarize the following raw CRM data into clean bullet points detailing competitor AI strategies."),
            ("human", "Raw CRM Data: {data}")
        ])

    def execute(self, raw_crm_data: str) -> str:
        chain = self.prompt | self.llm
        response = chain.invoke({"data": raw_crm_data})
        return response.content
