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

