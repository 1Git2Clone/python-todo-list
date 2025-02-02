"""
==============================================================================
Todo app made with PostgreSQL containing primitive functionality for creating
and editing tasks.
==============================================================================
"""

# ==============================================================================
# System libraries
# ==============================================================================

import sys

# ==============================================================================
# User defined libraries
# ==============================================================================

import psycopg2

# ==============================================================================
# Project files
# ==============================================================================

from utils import Categories, StatusCode
from utils.args import parse_args
from config import DB_NAME, DB_USERNAME
from database import Database
from utils.printing import print_category, print_db_row

# ==============================================================================
# Main
# ==============================================================================

def main() -> None:
    if not all([DB_NAME, DB_USERNAME]):
        sys.exit(StatusCode.NO_DOTENV_KEYS.value)

    args = parse_args()

    if not any(
        [args[args.update], args[args.show], args[args.all], args[args.task]]
    ) or (args[args.task] and any([args[args.show], args[args.all]])):
        print(
            "You need to specify at least one of these fields:",
            f"{', '.join([args.show, args.all, args.task])}",
            "\nAnd NOT all of them! You may only add or show tasks, not both.",
        )
        sys.exit(StatusCode.INVALID_ARGUMENTS.value)

    if all([args[args.show], args[args.all]]):
        print(
            "You can't show one and all tasks. Choose one of the two.",
        )
        sys.exit(StatusCode.INVALID_ARGUMENTS.value)

    db: Database = Database(psycopg2.connect(f"dbname={DB_NAME} user={DB_USERNAME}"))
    db.create_table_if_not_exists()

    if args[args.all]:
        for category in Categories:
            print()
            print_category(category.value)
            print_db_row(db, category.value)
        sys.exit(StatusCode.SUCCESS.value)

    if args[args.category] is None:
        print(
            f"Category is required for: {', '.join([f'--{arg}' for arg in [args.show, args.task]])}"
        )
        sys.exit(StatusCode.INVALID_ARGUMENTS.value)

    if args[args.update] is not None:
        id: int = int(str(args[args.update]))
        if args[args.task] is not None:
            db.update_task(id, str(args[args.category]), str(args[args.task]))
        else:
            db.update_task(id, str(args[args.category]))

    if args[args.task] is not None:
        print(f"Add task: {args[args.task]}")
        print(f"Category: {args[args.category]}")
        db.add_task(str(args[args.category]), str(args[args.task]))
        sys.exit(StatusCode.SUCCESS.value)

    if args[args.show] is not None:
        print_category(str(args[args.category]))
        print_db_row(db, str(args[args.category]))
        sys.exit(StatusCode.SUCCESS.value)

    sys.exit(StatusCode.SUCCESS.value)


if __name__ == "__main__":
    main()
