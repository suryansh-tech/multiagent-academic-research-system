from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from pathlib import Path
from dotenv import load_dotenv
from rich import print

load_dotenv(Path(__file__).resolve().parent / ".env")

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    results = tavily.search(query=query,max_results=5)

    out = []

    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    
    return "\n----\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

import arxiv

@tool
def academic_search(query: str) -> str:
    """Search the ArXiv academic database for published research papers. Use this tool heavily for science, technology, physics, math, and computer science topics. Returns Titles, Published Dates, Authors, PDF URLs and Abstracts."""
    try:
        client = arxiv.Client()
        search = arxiv.Search(
            query = query,
            max_results = 3,
            sort_by = arxiv.SortCriterion.Relevance
        )
        out = []
        for r in client.results(search):
            out.append(f"Title: {r.title}\nDate: {r.updated}\nURL: {r.entry_id}\nPDF: {r.pdf_url}\nAbstract: {r.summary[:800]}")
        if not out:
            return "No academic papers found."
        return "\n----\n".join(out)
    except Exception as e:
        return f"Error executing academic search: {str(e)}"
