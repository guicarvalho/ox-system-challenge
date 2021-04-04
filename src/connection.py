"""Functions to open and close database connections."""

import sqlite3
from contextlib import contextmanager
from sqlite3 import Connection


@contextmanager
def get_conn() -> Connection:
    """Create connection and commit/rollback before to close.

    Returns
    -------
        Database connection instance.
    """
    conn = sqlite3.connect("frigorifico.db")

    yield conn

    try:
        conn.commit()
    except Exception:
        conn.rollback()
    finally:
        conn.close()
