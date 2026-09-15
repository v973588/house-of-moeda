#!/usr/bin/env python3
"""
Library System CLI & Coordinator
Integrates catalog, storage, borrowing, and reporting modules into a cohesive application.
"""

import sys
from library_system.storage import load_books, save_books
from library_system.catalog import find_books_by_genre, find_books_by_author
from library_system.borrowing import checkout_book, return_book
from library_system.reporting import generate_library_summary, format_summary_report


def main():
    filepath = "sample_data.json"
    print(f"Loading catalog from {filepath}...")
    try:
        books = load_books(filepath)
    except Exception as e:
        print(f"Error loading catalog: {e}", file=sys.stderr)
        return 1

    summary = generate_library_summary(books)
    print("\n" + format_summary_report(summary) + "\n")

    print("--- Searching for Software Engineering books ---")
    se_books = find_books_by_genre(books, "software engineering")
    for b in se_books:
        status = "Available" if b.get("is_available") else "Borrowed"
        print(f"  [{b.get('id')}] {b.get('title')} ({b.get('year')}) - {status}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
