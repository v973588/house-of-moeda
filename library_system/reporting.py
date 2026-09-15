"""
Reporting Module (Module 4) - STARTER CODE (Contains Bug #4)
Responsible: Developer 4 / Branch: fix/reporting

BUG DESCRIPTION:
`generate_library_summary` has inverted the availability counters!
It is counting books where `is_available is False` as available, and books where `is_available is True` as borrowed.
As a result, reports report completely reversed stock numbers.
"""

from typing import List, Dict, Any


def generate_library_summary(books: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate comprehensive statistical summary of the library catalog.

    TODO (Dev 4): Fix the inverted availability counts!
    available_books should count books where is_available is True.
    borrowed_books should count books where is_available is False.
    """
    total = len(books)

    # BUG #4: Inverted boolean logic!
    available = sum(1 for b in books if b.get("is_available", False) is False)
    borrowed = sum(1 for b in books if b.get("is_available", False) is True)

    total_years = sum(book.get("year", 0) for book in books)
    avg_year = float(total_years / total) if total > 0 else 0.0

    all_genres = set()
    for book in books:
        for genre in book.get("genres", []):
            if isinstance(genre, str) and genre.strip():
                all_genres.add(genre.strip())

    return {
        "total_books": total,
        "available_books": available,
        "borrowed_books": borrowed,
        "average_year": avg_year,
        "unique_genres": sorted(list(all_genres))
    }


def format_summary_report(summary: Dict[str, Any]) -> str:
    """
    Format the summary dictionary into a clean, human-readable text report.
    """
    lines = [
        "========================================",
        "        LIBRARY STATUS REPORT           ",
        "========================================",
        f"Total Books Cataloged : {summary.get('total_books', 0)}",
        f"Available on Shelf    : {summary.get('available_books', 0)}",
        f"Currently Borrowed    : {summary.get('borrowed_books', 0)}",
        f"Average Release Year  : {summary.get('average_year', 0.0):.1f}",
        f"Unique Genres ({len(summary.get('unique_genres', []))}) : {', '.join(summary.get('unique_genres', []))}",
        "========================================"
    ]
    return "\n".join(lines)
