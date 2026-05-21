<div align="center">

# ⚡ AgentOS

**Enterprise Multi-Agent CRM Orchestrator**

[![CI/CD Pipeline](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square&logo=githubactions)](https://github.com/venkatasivanaga/AgentOS/actions)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

> A full-stack, containerized orchestrator that decomposes natural language tasks, routes subtasks to LangChain agents via CRM tool calls, and validates outputs through a strict Trust Layer.

---

</div>

## ✨ Key Features

- **🧠 LLM Task Routing:** Supervisor agent decomposes complex tasks into structured JSON execution plans using Pydantic.
- **🛡️ Einstein-Style Trust Layer:** Dedicated validation agent checks all outputs against original CRM payloads to strictly block hallucinations and toxic outputs.
- **⚡ Real-Time Telemetry:** TypeScript WebSocket middleware streams agent "thought processes" and execution latency directly to the client.
- **📊 Interactive UI:** React frontend visualizes the sub-agent routing steps live.
- **🐳 Enterprise Infrastructure:** Fully Dockerized with automated GitHub Actions CI/CD enforcing code quality and test coverage.

## 🏗️ Architecture Flow

```mermaid
graph TD
    %% Styling
    classDef user fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef agent fill:#2b6cb0,stroke:#2c5282,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef system fill:#2f855a,stroke:#276749,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef ui fill:#c05621,stroke:#9c4221,stroke-width:2px,color:#fff,rx:5px,ry:5px;

    U[👤 User Input]:::user --> S[🤖 Supervisor Agent]:::agent
    S -->|structured JSON| P[Task Router]:::system
    P -->|LangChain tool call| A1[🔍 CRM Search Agent]:::agent
    P -->|LangChain tool call| A2[📝 Opportunity Summarizer]:::agent
    P -->|Pydantic validation| A3[🛡️ Trust Validator]:::agent
    A1 --> SY[Data Synthesizer]:::system
    A2 --> SY
    A3 --> SY
    SY --> WS[🔌 WebSocket Server]:::system
    WS --> R[💻 React Trace Viewer]:::ui
  ```
  
## 🚀 Quickstart

Run the entire stack instantly using Docker Compose.

### Prerequisites
- Docker & Docker Compose
- Node.js 20+ (for local UI dev)
- Python 3.11+ (for local backend dev)

### Booting the Stack

```bash
# 1. Clone the repository
git clone [https://github.com/venkatasivanaga/AgentOS.git](https://github.com/venkatasivanaga/AgentOS.git)
cd AgentOS

# 2. Configure Environment
cp .env.example .env
# Edit .env and add your OpenAI API key

# 3. Launch the cluster
make run

The UI will be instantly available at http://localhost:3000.

```

## 📂 Codebase Structure

```
agentOS/
├── agents/                  # LangChain execution brains
│   ├── supervisor.py        # Task decomposition & routing
│   ├── search_agent.py      # CRM payload retrieval tools
│   ├── summarize_agent.py   # Exec brief generation
│   └── validate_agent.py    # Trust Layer hallucination checks
├── frontend/                # React Vite Application
│   └── src/AgentTrace.tsx   # Live step-viewer UI
├── server/                  # TypeScript Middleware
│   └── websocket_server.ts  # Broadcasts Python streams to React
├── schemas/                 # Pydantic structured output models
├── tests/                   # Pytest and Jest test suites
├── .github/workflows/       # CI/CD automated pipelines
├── docker-compose.yml       # Stack orchestration
└── Makefile                 # Dev ops shortcuts

```

## 🧪 Testing
This project enforces strict reliability with 40+ unit and integration tests across both languages.

```bash

# Run the full suite locally
make test
```


