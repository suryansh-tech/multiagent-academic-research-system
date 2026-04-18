<div align="center">

# Multi-Agent Academic Research System 🔬

![Version](https://img.shields.io/badge/version-v4.0.2-black?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange?style=for-the-badge)

*A deeply integrated, autonomous multi-agent architecture built to synthesize academic-grade research, conduct rigorous fact-checking loops, and generate massive technical reports. Wrapped in an uncompromising, high-density Brutalist interface.*

</div>

<br/>

## ⚡ Core Systems Integration

Our platform abandons basic LLM retrieval for a deterministic, cyclic, and heavily rigorous multi-agent pipeline. It operates sequentially to ensure data fidelity at every phase.

*   **Algorithmic Research Pipelines:** Dynamically switches execution depths. Choose from rapid indexing drafts to **Deep Dive Mode**—a massive computational loop involving recursive reading, structural drafting, adversarial critiquing, and factual verification.
*   **ArXiv Academic Ingestion:** Employs an autonomous decision state modifier. When technical subjects are requested, the Search Agent autonomously triggers the `arxiv` API to pull native abstracts and PDF URIs directly from peer-reviewed databases.
*   **Socratic Synthesizer:** Exogenous to standard reporting, this mode transforms complex paradigms into pedagogical scaffolds—forcing structural understanding over blind memorization.
*   **Local PDF Analysis Framework:** Natively ingest `.pdf` references globally alongside agentic web scraping utilizing rapid `PyMuPDF` tokenization.
*   **Brutalist Architectural UI:** A purely functional, deterministic grid layout eliminating consumer UI fluff. Exposes pure metadata, pipeline execution logs, and natively features Markdown, DocX, and PDF exportation pipelines.

## 🏗️ Architectural Execution Tree

The execution module relies on an asynchronous LangGraph graph configuration:
1.  **Search Node [Agent]:** Diagnoses the raw prompt. Determines API routings (e.g., standard `tavily` web queries vs. heavy `arxiv` paper indexing).
2.  **Reader Node [Agent]:** Scrapes raw HTML payloads from search outputs, filtering DOM noise.
3.  **Writer/Tutor Node [Agent]:** Aggregates cross-domain findings into densely structured semantic reports utilizing aggressive Markdown syntax constraints.
4.  **Adversarial Critic [Chain]:** Probes the raw draft for factual inconsistencies, logical gaps, and source misattribution.
5.  **Revision Writer [Chain]:** Iteratively mutates the draft based on adversarial feedback, magnifying depth.
6.  **Fact-Checker Node (Deep Dive Only):** The final sanitization protocol. Ensures strict factual alignment, appending explicit hyperlink provenance to all major assertions.

## 🚀 Deployment Operations

### Local Container Deployment
```bash
# 1. Clone the master repository
git clone https://github.com/suryansh-tech/academic-research-system.git
cd academic-research-system

# 2. Establish dependencies (Python 3.10+ required)
pip install -r requirements.txt
```

### Environment Variable Injection
Initialize a `.env` file within the system root. Your LLM pathways and search protocols require authentication.
```env
GOOGLE_API_KEY="your_gemini_pro_key"
TAVILY_API_KEY="your_tavily_search_key"
```

### Web Execution
```bash
streamlit run app.py
```

## ☁️ Cloud Node Deployment (Streamlit)
1. Push this repository to your tracking branch.
2. Navigate to [share.streamlit.io](https://share.streamlit.io) and grant repository access.
3. Define the Main File routing to `app.py`.
4. Inside Streamlit's **Advanced Settings**, parse your keys into the **Secrets manager**:
```toml
GOOGLE_API_KEY="your_gemini_pro_key"
TAVILY_API_KEY="your_tavily_search_key"
```
5. Execute **Deploy**.

## 🛠️ Stack Specifications
*   **Core Logic Operations:** Python, LangChain, LangGraph
*   **Intelligence Provider:** Google DeepMind (Gemini 2.5 Flash-Lite)
*   **Retrieval Systems:** Tavily Search API, ArXiv API, BeautifulSoup4
*   **Frontend Engine:** Streamlit (Custom Grid CSS Virtualization)
*   **Document Parsers:** PyMuPDF, Python-DocX
