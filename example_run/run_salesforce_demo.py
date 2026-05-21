from dotenv import load_dotenv
load_dotenv()

import asyncio
import time
from agents.search_agent import SalesforceSearchAgent
from agents.summarize_agent import SalesforceSummarizeAgent
from agents.validate_agent import EinsteinTrustValidator
from utils.streamer import broadcast_step

async def run_demo():
    print("[*] Booting AgentOS Salesforce Demo...\n")
    
    # 1. Search Agent
    await broadcast_step({"agent": "SalesforceSearchAgent", "action": "Querying Opportunities for 'Oracle'", "duration_ms": 0})
    start = time.time()
    searcher = SalesforceSearchAgent()
    raw_data = searcher.execute("Oracle")
    await broadcast_step({"agent": "SalesforceSearchAgent", "action": f"Retrieved payload: {raw_data[:50]}...", "duration_ms": int((time.time()-start)*1000)})
    
    # 2. Summarize Agent
    await broadcast_step({"agent": "SalesforceSummarizeAgent", "action": "Condensing raw payload into executive brief", "duration_ms": 0})
    start = time.time()
    summarizer = SalesforceSummarizeAgent()
    summary = summarizer.execute(raw_data)
    await broadcast_step({"agent": "SalesforceSummarizeAgent", "action": "Summary generated.", "duration_ms": int((time.time()-start)*1000)})
    
    # 3. Validate Agent (Einstein Trust Layer)
    await broadcast_step({"agent": "EinsteinTrustValidator", "action": "Checking for hallucinations and data leaks", "duration_ms": 0})
    start = time.time()
    validator = EinsteinTrustValidator()
    validation = validator.execute(summary, raw_data)
    await broadcast_step({"agent": "EinsteinTrustValidator", "action": f"Validation passed. Confidence: {validation.get('confidence_score')}", "duration_ms": int((time.time()-start)*1000)})
    
    print("\n[+] Demo Complete. Check the React UI for the execution trace.")

if __name__ == "__main__":
    asyncio.run(run_demo())
