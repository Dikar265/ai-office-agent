"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

import asyncio
import os
import uuid
from typing import Any, Callable, List, Optional, cast

import markdown
from langchain_tavily import TavilySearch
from langgraph.runtime import get_runtime
from playwright.sync_api import sync_playwright

from react_agent.context import Context


async def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    runtime = get_runtime(Context)
    wrapped = TavilySearch(max_results=runtime.context.max_search_results, include_images=True)
    return cast(dict[str, Any], await wrapped.ainvoke({"query": query}))

def render_html(content: str, title: str) -> str:
    # 1. Convertimos los corchetes de seguridad de la IA a HTML real
    seguro_html = content.replace("[", "<").replace("]", ">")
    
    final_body = markdown.markdown(seguro_html)
    
    # 2. Cargamos el template
    with open("templates/base.html", "r", encoding="utf-8") as f:
        template = f.read()

    # 3. Inyectamos los datos (usando replace para evitar fallos de .format con JS/CSS)
    return template.replace("{title}", title).replace("{content}", final_body)

def run_playwright(content: str, title: str) -> str:
    OUTPUT_DIR = "outputs"

    os.makedirs("outputs", exist_ok=True)
    file_name = f"report_{uuid.uuid4().hex}.pdf"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    final_html = render_html(content, title)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.set_content(final_html, wait_until="networkidle")

        page.wait_for_timeout(2000)

        page.pdf(
            path=file_path,
            format="A4",
            print_background=True,
        )

        browser.close()

    return file_path


async def generate_pdf(content: str, title: str) -> str: 
    """Generate a PDF file with a dynamic title and content."""
    loop = asyncio.get_running_loop()

    file_path = await loop.run_in_executor(
        None,
        lambda: run_playwright(content, title)
    )
    return file_path


TOOLS: List[Callable[..., Any]] = [search, generate_pdf]
