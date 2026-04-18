# Multi-Agent Academic Research System 🔬

![Version](https://img.shields.io/badge/version-v4.0.2-black)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange)

An open-source, multi-agent AI architecture engineered to synthesize academic-grade research, conduct rigorous fact-checking, and generate comprehensive technical reports. Wrapped in a high-density, Brutalist UI framework.

## ⚡ Features

*   **Modular Multi-Agent Pipeline:** Built atop LangGraph, featuring specialized agents (Search, Reader, Writer, Critic, and Fact Checker) operating in a multi-stage cyclic workflow.
*   **ArXiv Deep Integration:** Autonomous agentic selection to query and ingest published STEM/academic papers via the ArXiv API.
*   **Variable Depth Processing:** Ranging from quick search drafts to **Deep Dive Mode** (Standard synthesis + rigorous critique loops + terminal fact-checking).
*   **Socratic Tutor Mode:** Transforms raw data into pedagogical outlines and critical thinking exercises.
*   **Local PDF Ingestion:** Natively parse reference material globally alongside agentic web scraping via `PyMuPDF`.
*   **Brutalist Architectural UI:** A purely functional, grid-based interface with native Markdown, DocX, and PDF export functionality.

## 🏗️ Architecture

The system utilizes an asynchronous LangGraph execution chain:
1.  **Search Agent:** Evaluates the topic. Uses `tavily` for general queries or `arxiv` for highly technical/academic prompts.
2.  **Reader Agent:** Scrapes raw HTML payloads from returned URLs and filters noise.
3.  **Writer/Tutor Agent:** Aggregates findings into heavily-structured Notion-style Markdown reports.
4.  **Critic Chain:** Evaluates the original draft for factual holes, logical flow, and academic rigor.
5.  **Revision Writer:** Expands and rewrites the draft iteratively based on the critic's feedback.
6.  **Fact-Checker (Deep Dive Only):** A final, ruthless verification layer ensuring all statements carry source attribution.

## 🚀 Installation & Local Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/suryansh-tech/academic-research-system.git
cd academic-research-system
```

### 2. Install Dependencies
Ensure you are running Python 3.10+.
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory. The agents require API keys for LLM execution and web scraping.
```env
GOOGLE_API_KEY="your_gemini_pro_key"
TAVILY_API_KEY="your_tavily_search_key"
```

### 4. Run the Interface
```bash
streamlit run app.py
```

## ☁️ Cloud Deployment (Streamlit)
1. Fork or push this repository to your GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and link your repository.
3. Set your Main File path to `app.py`.
4. In Streamlit's **Advanced Settings**, add your API keys to the **Secrets** manager:
```toml
GOOGLE_API_KEY="your_gemini_pro_key"
TAVILY_API_KEY="your_tavily_search_key"
```
5. Click **Deploy**.

## 🛠️ Technology Stack
*   **Core:** Python, LangChain, LangGraph
*   **LLM Provider:** Google DeepMind (Gemini 2.5 Flash-Lite)
*   **Search/Scraping:** Tavily Search API, ArXiv API, BeautifulSoup4
*   **UI Framework:** Streamlit (Custom CSS Override)
*   **Processing:** PyMuPDF, Python-DocX

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
