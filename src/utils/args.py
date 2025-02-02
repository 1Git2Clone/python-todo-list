"""
==============================================================================
Custom argument class and `parse_args()` function.
==============================================================================
"""

from dataclasses import dataclass
from argparse import ArgumentParser, Namespace
from typing import Any, Optional

from utils import Categories


@dataclass(init=True, frozen=True)
class Args:
    args: Namespace

    # ==========================================================================
    # Required
    # ==========================================================================

    category: str = "category"

    # ==========================================================================
    # Not required
    # ==========================================================================

    show: str = "show"
    remove: str = "remove"
    all: str = "all"
    task: str = "task"
    update: str = "update"

    # ==========================================================================
    # Helper methods
    # ==========================================================================

    def __getitem__(self, arg: str) -> Optional[Any]:
        try:
            return self.args.__dict__[arg]
        except KeyError:
            return None


def parse_args() -> Args:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        f"-{Args.category[:3]}",
        f"--{Args.category}",
        type=str,
        choices=[c.value for c in Categories],
    )
    parser.add_argument(
        f"-{Args.show[0]}",
        f"--{Args.show}",
        action="store_true",
        help="List tasks from category",
    )
    parser.add_argument(
        f"-{Args.remove[0]}",
        f"--{Args.remove}",
        action="store_true",
        help="Remove tasks from category",
    )
    parser.add_argument(
        f"-{Args.all[0]}",
        f"--{Args.all}",
        action="store_true",
        help="Goes through all categories",
    )
    parser.add_argument(
        f"--{Args.task}",
        type=str,
        help="Task to add (required if --show is not set)",
    )
    parser.add_argument(
        f"-{Args.update[0]}",
        f"--{Args.update}",
        type=int,
        help="Task ID update",
    )

    return Args(args=parser.parse_args())
