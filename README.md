# AgentOS — Multi-Agent Workflow Orchestrator

> A supervisor-agent system that decomposes natural language tasks,
> routes subtasks to specialized agents via tool calls, and synthesizes
> final responses in real time.

## Architecture
```mermaid
graph TD
    U[User Input] --> S[Supervisor Agent]
    S -->|decompose| P[Task Planner]
    P -->|route| A1[Search Agent]
    P -->|route| A2[Summarize Agent]
    P -->|route| A3[Validate Agent]
    A1 --> SY[Synthesizer]
    A2 --> SY
    A3 --> SY
    SY --> WS[WebSocket Server]
    WS --> R[React Frontend]
## Quickstart
git clone https://github.com/venkatasivanaga/AgentOS.git
cd AgentOS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
npm run start:ws
## Test Coverage
40 tests covering routing, tool calls, and failure recovery.
