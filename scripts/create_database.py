"""Create database."""

from src.connection import get_conn

with get_conn() as conn:
    cursor = conn.cursor()
    cursor.execute(
        "create table if not exists boi (identificador integer not null, peso real not null, raca text not null );"
    )
