"""
Catalog Module (Module 1) - STARTER CODE (Contains Bug #1)
Responsible: Developer 1 / Branch: fix/catalog

BUG DESCRIPTION:
1. `find_books_by_genre` currently performs a strict case-sensitive match.
   Searching for "software engineering" or "PYTHON" fails to match "Software Engineering" or "Python".
2. `calculate_average_year` performs integer division `//` instead of float division `/`,
   and crashes if books list is empty!
"""

from typing import List, Dict, Any, Optional


def validate_book(book: Dict[str, Any]) -> bool:
    """
    Validate that a book dictionary has the required structure and non-empty values.
    """
    if not isinstance(book, dict):
        raise ValueError("Book entry must be a dictionary")

    required_fields = ["id", "title", "author", "year", "genres"]
    for field in required_fields:
        if field not in book:
            raise ValueError(f"Missing required field: '{field}'")

    if not isinstance(book["id"], int) or book["id"] <= 0:
        raise ValueError("Field 'id' must be a positive integer")

    if not isinstance(book["title"], str) or not book["title"].strip():
        raise ValueError("Field 'title' cannot be empty")

    if not isinstance(book["author"], str) or not book["author"].strip():
        raise ValueError("Field 'author' cannot be empty")

    if not isinstance(book["year"], int) or book["year"] <= 0:
        raise ValueError("Field 'year' must be a positive integer")

    if not isinstance(book["genres"], list) or len(book["genres"]) == 0:
        raise ValueError("Field 'genres' must be a non-empty list of strings")

    return True


def find_books_by_genre(books: List[Dict[str, Any]], genre: str) -> List[Dict[str, Any]]:
    """
    Find all books that belong to a specific genre.

    TODO (Dev 1): Fix case-sensitivity bug!
    Currently this only matches if the case matches exactly.
    Make it match case-insensitively (e.g. 'software engineering' should match 'Software Engineering').
    """
    if not genre or not genre.strip():
        return []

    # BUG #1A: Exact match fails when user searches with lowercase or uppercase!
    # Expected: compare normalized strings using .lower()
    return [
        book for book in books
        if genre in book.get("genres", [])
    ]


def find_books_by_author(books: List[Dict[str, Any]], author_query: str) -> List[Dict[str, Any]]:
    """
    Find all books whose author contains the query string (case-insensitive substring match).
    """
    if not author_query or not author_query.strip():
        return []

    target = author_query.strip().lower()
    return [
        book for book in books
        if target in book.get("author", "").lower()
    ]


def calculate_average_year(books: List[Dict[str, Any]]) -> float:
    """
    Calculate the average publication year of books in the catalog.

    TODO (Dev 1): Fix division and empty list handling!
    Currently uses integer division '//' and does not handle empty list safely.
    """
    # BUG #1B: Missing empty check crashes, and integer division loses precision!
    total_years = sum(book.get("year", 0) for book in books)
    return total_years // len(books)
