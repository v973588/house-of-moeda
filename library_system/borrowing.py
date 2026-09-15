from typing import List, Dict, Any, Optional


def checkout_book(
    books: List[Dict[str, Any]],
    book_id: int,
    borrower_name: str
) -> Dict[str, Any]:
    """
    Check out a book to a borrower.
    """
    if not borrower_name or not borrower_name.strip():
        raise ValueError("Borrower name cannot be empty")

    target_book = None
    for book in books:
        if book.get("id") == book_id:
            target_book = book
            break

    if target_book is None:
        raise ValueError(f"Book with ID {book_id} not found in catalog")

    if not target_book.get("is_available", False):
        raise ValueError(
            f"Book '{target_book.get('title')}' (ID: {book_id}) is currently unavailable"
        )

    # Fix: mark the book as unavailable after checkout
    target_book["is_available"] = False
    target_book["borrower"] = borrower_name.strip()

    return {
        "book_id": book_id,
        "title": target_book.get("title"),
        "borrower": borrower_name.strip(),
        "status": "CHECKED_OUT"
    }


def return_book(books: List[Dict[str, Any]], book_id: int) -> Dict[str, Any]:
    """
    Return a currently borrowed book back to the library catalog.
    """
    target_book = None
    for book in books:
        if book.get("id") == book_id:
            target_book = book
            break

    if target_book is None:
        raise ValueError(f"Book with ID {book_id} not found in catalog")

    if target_book.get("is_available", False) is True:
        raise ValueError(
            f"Book '{target_book.get('title')}' (ID: {book_id}) is already in library (not checked out)"
        )

    former_borrower = target_book.pop("borrower", "Unknown")
    target_book["is_available"] = True

    return {
        "book_id": book_id,
        "title": target_book.get("title"),
        "former_borrower": former_borrower,
        "status": "RETURNED"
    }


def calculate_late_fee(days_overdue: int, daily_rate: float = 0.50) -> float:
    """
    Calculate late fee penalty based on overdue days.
    """
    if days_overdue <= 0:
        return 0.0
    return round(float(days_overdue * daily_rate), 2)
