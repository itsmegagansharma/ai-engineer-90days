"""
Day 38 · Task 1: Parse files

Read PDFs with pypdf, DOCX with python-docx, HTML with BeautifulSoup.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install pypdf python-docx beautifulsoup4
from pathlib import Path
from pypdf import PdfReader


def load_pdf(path: Path) -> list[dict]:
    """Return one dict per page: {"text": ..., "source": filename, "page": n}"""
    # TODO
    pass


def load_docx(path: Path) -> list[dict]:
    # TODO: use docx.Document(path).paragraphs
    pass
