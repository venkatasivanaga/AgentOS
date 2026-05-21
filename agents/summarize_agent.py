from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

class SalesforceSummarizeAgent:
    """Transforms raw Salesforce JSON payloads into formatted executive briefings."""
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.2)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an executive assistant inside Salesforce. Summarize the following raw CRM data into clean bullet points detailing competitor AI strategies."),
            ("human", "Raw CRM Data: {data}")
        ])

    def execute(self, raw_crm_data: str) -> str:
        chain = self.prompt | self.llm
        response = chain.invoke({"data": raw_crm_data})
        return response.content
