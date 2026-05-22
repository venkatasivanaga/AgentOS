## ⚡ AgentOS

AgentOS is a multi-agent demo that simulates Salesforce-style CRM workflows with:

- a **Python agent pipeline** (search → summarize → validate),
- a **TypeScript WebSocket server** for streaming step updates, and
- a **React UI** for live execution traces.

## ✨ Features

- **Supervisor planning** with structured output (`ExecutionPlan`) via Pydantic schemas.
- **Search agent** that returns mocked CRM opportunity payloads.
- **Summarization agent** that converts raw JSON into an executive-style summary.
- **Trust validation agent** that checks summary alignment against original data.
- **Live trace UI** that subscribes to streamed step events over WebSocket.

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
  
## 🏗️ How it works

1. Python demo code runs the agent sequence in `example_run/run_salesforce_demo.py`.
2. Each step is broadcast to `ws://localhost:8080` via `utils/streamer.py`.
3. `server/websocket_server.ts` rebroadcasts messages to connected clients.
4. `frontend/src/AgentTrace.tsx` renders incoming events in real time.

## 📦 Prerequisites

- Python 3.11+
- Node.js 20+
- npm

If you use LLM-backed paths (for example supervisor/summarize/validate flows), configure `.env` from `.env.example`.

## 🚀 Quick start (local development)

```bash
# 1) Clone and enter the repo
git clone https://github.com/venkatasivanaga/AgentOS.git
cd AgentOS

# 2) Environment
cp .env.example .env

# 3) Install dependencies
python3 -m pip install -r requirements.txt
npm ci
```

Start components in separate terminals:

```bash
# Terminal A: WebSocket server
npm run start:ws

# Terminal B: React UI (http://localhost:3000)
npm run dev

# Terminal C: Python demo that streams steps
PYTHONPATH=. python3 example_run/run_salesforce_demo.py
```

## 🐳 Docker

You can also run services with Docker Compose:

```bash
docker compose up --build
```

This starts the backend demo container and WebSocket server.  
For local UI development, run `npm run dev` on the host.

## 🧪 Testing

Run the currently maintained test suites:

```bash
# TypeScript tests
npm test -- --runInBand

# Python schema/routing tests
python3 -m pytest tests
```

## 📂 Repository structure

```text
agents/         Python agents (supervisor/search/summarize/validate)
schemas/        Pydantic models for routing plans
utils/          Python streaming utilities
server/         TypeScript WebSocket middleware
frontend/       React UI (Vite)
example_run/    Runnable demos and exploratory scripts
tests/          Jest + pytest tests
```

