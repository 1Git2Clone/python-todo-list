"""
==============================================================================
Project configuration data.
==============================================================================
"""

import os
import dotenv

# ==============================================================================
# Generic configuration
# ==============================================================================

DB_TABLE_NAME: str = "task_list"
PROJECT_ROOT: str = os.path.dirname(os.path.dirname(__file__))

# ==============================================================================
# Environment configuration
# ==============================================================================

DOTENV_FILE_NAME: str = ".env"
DOTENV_PATH: str = os.path.join(PROJECT_ROOT, DOTENV_FILE_NAME)
DB_NAME: str | None = dotenv.get_key(DOTENV_PATH, "DB_NAME")
DB_USERNAME: str | None = dotenv.get_key(DOTENV_PATH, "DB_USERNAME")
