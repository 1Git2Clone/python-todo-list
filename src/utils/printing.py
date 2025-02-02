"""
==============================================================================
Printing utility functions.
==============================================================================
"""

from typing import SupportsIndex

from database import Database


def print_category(
    category: str, width: SupportsIndex = 80, fill_char: str = " "
) -> None:
    print(
        ("-" * width),
        f"{category.upper()} TASKS".center(width, fill_char),
        ("-" * width),
        sep="\n",
    )


def print_db_row(db: Database, category: str) -> None:
    print("\n".join([f"ID {row[0]}: {row[2]}" for row in db.get_tasks(category)]))
