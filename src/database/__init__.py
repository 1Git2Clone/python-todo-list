"""
==============================================================================
Database class for managing the data.
==============================================================================
"""

from dataclasses import dataclass
from typing import Any

from psycopg2.extensions import connection, cursor

from config import DB_TABLE_NAME


@dataclass(init=True, frozen=True)
class DbEntries:
    id: str = "id"
    category: str = "category"
    task: str = "task"


@dataclass(init=False)
class Database:
    conn: connection
    cur: cursor
    entries: DbEntries = DbEntries()

    def __init__(self, conn: connection) -> None:
        self.conn = conn
        self.cur = self.conn.cursor()

    # Very important to do for correctness reasons.
    def __del__(self) -> None:
        self.cur.close()
        self.conn.close()

    def create_table_if_not_exists(self) -> None:
        self.cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME}(
                {self.entries.id} SERIAL PRIMARY KEY,
                {self.entries.category} VARCHAR(255) NOT NULL,
                {self.entries.task} TEXT NOT NULL
            );
            """)
        self.conn.commit()

    def print_schema(self) -> None:
        """
        !(DEBUG ONLY)
        A function that prints the schema of the current database.
        """
        self.cur.execute(f"""
        SELECT column_name, data_type, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = '{DB_TABLE_NAME}';
        """)
        print("\n".join([str(row) for row in self.cur.fetchall()]))

    def add_task(self, category: str, task_desciption: str) -> None:
        query: str = f"""
            INSERT INTO {DB_TABLE_NAME} ({self.entries.category}, {self.entries.task})
            VALUES (%s, %s);
        """
        params: tuple[str, str] = (category, task_desciption)
        self.cur.execute(query, params)
        self.conn.commit()

    def update_task(
        self, id: int, new_category: str, new_description: str | None = None
    ) -> None:
        query: str
        params: tuple[str, str, int] | tuple[str, int]

        if new_description is not None:
            query = f"""
                UPDATE {DB_TABLE_NAME}
                SET {self.entries.category} = %s,
                    {self.entries.task} = %s
                WHERE {self.entries.id} = %s;
            """
            params = (new_category, new_description, id)
        else:
            query = f"""
                UPDATE {DB_TABLE_NAME}
                SET {self.entries.category} = %s
                WHERE {self.entries.id} = %s;
            """
            params = (new_category, id)
        self.cur.execute(query, params)
        self.conn.commit()

    def get_tasks(self, target_category: str) -> list[tuple[Any, ...]]:
        query: str = f"""
            SELECT *
            FROM {DB_TABLE_NAME}
            WHERE {self.entries.category} = %s;
            """
        params: tuple[str] = (target_category,)
        self.cur.execute(query, params)
        return self.cur.fetchall()
