# 🌌 Vantage-Point 2.0: Autonomous Enterprise Treasury

**Vantage-Point 2.0** is an AI-native autonomous treasury engine built for the **Vultr x Gemini Hackathon**. It solves the "$1.2 Trillion SMB Cash Drag" by transforming idle corporate capital into yield-bearing assets through an agentic boardroom orchestration.

🟢 **Live Demo (Vultr Hosted):** [http://216.128.155.55](http://216.128.155.55)

---

## 🏛 The Multi-Agent Architecture

Vantage-Point uses a **"Council of Experts"** approach to financial decision-making, ensuring every trade is audited for risk and compliance before execution.

```mermaid
graph TD
    A[Financial Event: Invoice/Payroll] --> B{Boardroom Council}
    B --> C[🦁 CEO: Gemini 1.5 Flash]
    B --> D[⚖️ General Counsel: DeepSeek-V3]
    B --> E[📉 Risk Officer: Qwen-2.5-72B]
    B --> I[⚙️ Operations Agent: Vultr Inference (Llama 3)]
    C -->|Synthesis| F[Decision: BUY/SELL/HOLD]
    F -->|Execution| G[Kraken CLI: xStocks Layer]
    G --> H[Vantage Portfolio Dashboard]
    D -.->|Compliance Audit| C
    E -.->|Volatility Check| C
    I -.->|Operational Metrics| C
```

### 🧠 Open-Source LLM Integration (via Featherless)

To meet the challenge of "realistic future-of-work use cases," we leverage specialized open-source models:

- **DeepSeek-V3**: Powers the **General Counsel** for strict logical auditing and compliance verification.
- **Qwen-2.5-72B**: Powers the **Macro Strategist**, providing deep contextual reasoning on market volatility.
- **Llama 3 8B (via Vultr Serverless Inference)**: Powers the **Operations Agent**, demonstrating seamless multi-cloud LLM orchestration.

---

## 🏆 Hackathon Challenge Alignments

Vantage-Point 2.0 was explicitly built to seamlessly integrate all five technology partners into a unified, enterprise-grade autonomous workflow:

### 1. ☁️ Vultr (Enterprise Infrastructure & Serverless Inference)
- **Vultr VM Backend Deployment**: The system of record and execution engine is deployed natively on a Vultr cloud instance, orchestrated via Docker.
- **Vultr Serverless Inference**: Powers the **Operations Agent (Llama 3 8B)**, demonstrating seamless multi-cloud LLM orchestration.

### 2. 🧠 Google Gemini (Advanced Reasoning & Multimodal)
- **CEO Agent**: Powered by **Gemini 1.5 Flash/Pro**, this agent handles complex, multi-step decision-making, synthesizing input from the entire boardroom council to form a final execution strategy.
- **Multimodal Intelligence**: Analyzes visual business reports and static financial documents to unlock richer interactions.

### 3. 🐙 Kraken (Programmatic xStocks Execution)
- **Kraken CLI**: Acts as the execution layer. The agent forms a strategy and programmatically executes trades on tokenized U.S. equities (**xStocks**) without any human intervention.

### 4. 🪶 Featherless (Domain-Specialized Open-Source Agents)
- **General Counsel (DeepSeek-V3)**: A domain-specialized compliance auditor running via Featherless Serverless Inference.
- **Macro Strategist (Qwen-2.5-72B)**: A domain-specialized risk officer providing deep contextual reasoning on market volatility.

### 5. 🎙️ Speechmatics (Voice-Powered Executive Interface)
- **Real-Time Voice Ingestion**: Executives can verbally dictate market strategies or submit voice-memos of urgent financial events. Speechmatics transcribes this audio in real-time, converting unstructured speech into actionable "Float Events" for the autonomous boardroom.

---

## ✨ Key Features

- **📜 Glass-Box Reasoning**: A "SOX-ready" audit trail for every AI decision.
- **📈 Equinox Score**: Real-time treasury efficiency metric.
- **🛡️ Defensive Failover**: Resilient architecture with 120s timeouts for complex reasoning.
- **🎨 Premium Aesthetics**: A state-of-the-art glassmorphism UI designed for executive oversight.

---

## 🛠 Tech Stack

- **AI Models**: Gemini 1.5 Flash, DeepSeek-V3, Qwen-2.5-72B, Llama 3 8B.
- **APIs**: Vultr Serverless Inference, Featherless API, Speechmatics API, Google AI Studio.
- **Backend**: FastAPI, MongoDB, Kraken CLI v0.3.2.
- **Frontend**: React (Vite), TypeScript, Nginx.
- **Infrastructure**: Docker, Docker Compose, Vultr Cloud.

---

## 🚀 Deployment (Vultr)

### 1-Line Provisioning

On a fresh Vultr Ubuntu instance:

```bash
curl -sSL https://raw.githubusercontent.com/rasali535/vantage_point/main/vultr-init.sh | sudo bash
```

### Manual Setup

1. **Clone**: `git clone https://github.com/rasali535/vantage_point.git`
2. **Configure**: Fill in `.env` with API keys.
3. **Launch**: `docker-compose up --build -d`

---

Built with precision by **Ras Ali Labs** for the **AI Agent Olympics Hackathon