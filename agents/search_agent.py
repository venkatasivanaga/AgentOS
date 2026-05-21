import json
from langchain_core.tools import tool

class SalesforceSearchAgent:
    """Simulates deep search against Salesforce Account and Opportunity standard objects."""
    
    @tool
    def query_salesforce_records(object_type: str, search_term: str) -> str:
        """Queries the Salesforce database for matching Accounts, Opportunities, or Leads."""
        # Mocked highly structured CRM payloads mirroring real Salesforce REST API responses
        mock_database = {
            "opportunity": [
                {"Name": "HubSpot Enterprise Migration", "StageName": "Discovery", "Amount": 1200000, "AI_Strategy": "Deep inbound automation via ChatSpot"},
                {"Name": "Microsoft Dynamics Expansion", "StageName": "Proposal", "Amount": 2500000, "AI_Strategy": "Native Copilot workspace embedding"},
                {"Name": "Oracle CX Modernization", "StageName": "Negotiation", "Amount": 1800000, "AI_Strategy": "Generative AI sales workflow orchestration"}
            ]
        }
        
        normalized_type = object_type.lower()
        if normalized_type in mock_database:
            results = [rec for rec in mock_database[normalized_type] if search_term.lower() in rec["Name"].lower()]
            return json.dumps(results)
        return json.dumps({"error": f"Object type {object_type} not found in Salesforce schema."})

    def execute(self, instruction: str) -> str:
        # Grounding the tool invocation
        return self.query_salesforce_records.invoke({"object_type": "opportunity", "search_term": instruction})
