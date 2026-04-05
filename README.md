# 🧠 AI Office Agent (LangGraph + Playwright + PDF Generator)

## ⚡ Quick Start

```bash
cp .env.example .env (config the env)
docker compose up --build
```

### Option 1: Using LangSmith Studio (recommended)

https://smith.langchain.com/studio/?baseUrl=http://0.0.0.0:2024

### Option 2: Direct local access
- http://localhost:2024
- http://127.0.0.1:2024

> ⚠️ Note:
> - `0.0.0.0` works when used as `baseUrl` in LangSmith Studio  
> - It does **NOT** work directly in the browser  

 ### The agent workflow:

1. Receives a query  
2. Searches information  
3. Processes results  
4. Generates a PDF report  

Example:

```
User: "Create a summary about FastAPI and generate a report"
```

Output:

```
/outputs/report_xxxxx.pdf
```

---
An intelligent **ReAct-based AI agent** built with LangGraph capable of:

- 🔎 Searching the web  
- 🧠 Reasoning over results  
- 📄 Generating PDF reports automatically  
- 🐳 Running fully in Docker  
- 🤖 Integrating with local LLMs via Ollama  

---

## 🚀 Features

- **ReAct Agent (LangGraph)**  
  Iterative reasoning: think → act → observe → answer  

- **Web Search (Tavily)**  
  Real-time search with enriched results  

- **HTML → PDF (Playwright)**  
  Converts dynamic content into professional PDFs  

- **HTML Template System**  
  Uses `templates/base.html` for structured reports  

- **Full Docker Support**  
  Includes:
  - Agent  
  - Ollama (local LLM)  

- **Unique File Generation (UUID)**  
  Prevents filename collisions  

- **Observability (LangSmith)**  
  Full tracing and debugging of agent executions  
---

## 🧱 Project Structure

```
.
├── src/react_agent/
│   ├── graph.py
│   ├── tools.py
│   ├── context.py
│   ├── prompts.py
│   └── state.py
│
├── templates/
│   └── base.html
│
├── outputs/
├── ollama/
├── docker-compose.yml
└── Dockerfile
```

---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone https://github.com/Dikar265/ai-office-agent.git
cd ai-office-agent
```

---

### 2. Environment variables

```bash
cp .env.example .env
```

Example:

```
TAVILY_API_KEY=your_key
OPENAI_API_KEY=your_key (optional)
```

---

### 3. Run with Docker

```bash
docker compose up --build
```
---
## 🌐 Accessing LangGraph Studio

By default, the agent may bind to `0.0.0.0`, which is required for Docker networking.  
However, when accessing LangGraph Studio from your browser, you should use:


- http://localhost:2024  
- http://127.0.0.1:2024  


> ⚠️ If you try to access using `0.0.0.0`, it will not work in the browser.

---

### 🐳 Docker Note

- `0.0.0.0` → used internally for container binding  
- `localhost / 127.0.0.1 → used from your machine/browser  

---

## 🛠 Available Tools

### 🔎 `search(query)`
- Uses Tavily  
- Returns web results + images  

---

### 📄 `generate_pdf(content, title)`
- Converts markdown → HTML  
- Injects into template  
- Generates PDF using Playwright  

---

## 🧩 How PDF Generation Works

1. Agent generates markdown content  
2. Converted to HTML  
3. Injected into `base.html`  
4. Rendered with Playwright  
5. Exported as PDF  

---

## 📊 Observability (LangSmith)

This project integrates with **LangSmith** to monitor and debug agent behavior in real time.

- 🔍 Visualize each step of the ReAct loop  
- 🧠 Inspect reasoning and decision-making  
- 🛠 Debug tool calls and outputs  
- 📈 Analyze performance and latency  

---

### Setup

Add the following to your `.env`:

```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=ai-office-agent
```

---

## 🐳 Ollama (Local LLM)

Runs at:

```
http://localhost:11434
```

Supported models:

- mistral  
- llama3  
- phi  

---

## 🔧 Customization

- ➕ Add new tools (`tools.py`)  
- 🧠 Change model (OpenAI / Ollama)  
- 🎨 Improve HTML template  
- 🔄 Modify agent logic (`graph.py`)  

---

## 📌 Roadmap

- [ ] Streaming responses  
- [ ] Multi-agent system  
- [ ] RAG with pgvector  
- [ ] Web UI (React / Next.js)  
- [ ] History persistence  

---

## 🧠 Tech Stack

- LangGraph  
- LangChain  
- LangSmith  
- Playwright  
- Docker  
- Ollama  
- Python 3.12  

---