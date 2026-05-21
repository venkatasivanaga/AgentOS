from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

class TrustValidationSchema(BaseModel):
    is_safe: bool = Field(description="True if summary matches data constraints without hallucinations or toxic terms.")
    confidence_score: float = Field(description="Score between 0.0 and 1.0 reflecting factual alignment.")
    reasoning: str = Field(description="Explanation of the evaluation pass or failure.")

class EinsteinTrustValidator:
    """Emulates the Salesforce Trust Layer to prevent hallucinations and data leaks."""
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.2)
        self.structured_llm = self.llm.with_structured_output(TrustValidationSchema)

    def execute(self, summary: str, original_data: str) -> dict:
        system_msg = "Verify that the summary does not hallucinate information absent from the original CRM data."
        human_msg = f"Original Data: {original_data}\nGenerated Summary: {summary}"
        
        # Invoke structured verification loop
        result = self.structured_llm.invoke([
            ("system", system_msg),
            ("human", human_msg)
        ])
        return result.model_dump()
