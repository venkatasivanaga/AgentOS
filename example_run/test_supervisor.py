import json
from dotenv import load_dotenv
from agents.supervisor import SupervisorAgent

load_dotenv()

if __name__ == "__main__":
    supervisor = SupervisorAgent()
    sample_task = "Research the top 3 competitors to Salesforce and summarize their AI strategy in bullet points"
    
    print(f"[*] Task: {sample_task}\n")
    plan = supervisor.decompose_task(sample_task)
    print("[*] Execution Plan:")
    print(json.dumps(plan, indent=2))
