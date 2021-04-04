"""Data access layer methods."""

from connection import get_conn
from model import Ox


def create(identifier: int, weight: float, breed: str) -> None:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO boi (identificador, raca, peso) VALUES (?,?,?)", (identifier, breed, weight))


def update(identifier: int, weight: float, breed: str) -> None:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("update boi set raca=?, peso=? where identificador=?;", (breed, weight, identifier))


def get(identifier: int) -> Ox:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT identificador, raca, peso FROM boi WHERE identificador = ?;", (identifier,))

        line = cursor.fetchone()

        return Ox(identifier=line[0], breed=line[1], weight=line[2])


def list_all() -> list[Ox]:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT identificador, raca, peso FROM boi;")

        return [Ox(identifier=line[0], breed=line[1], weight=line[2]) for line in cursor.fetchall()]


def delete(identifier: int) -> None:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM boi WHERE identificador=?", (identifier,))


def get_fatter() -> Ox:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT identificador, raca, peso FROM boi ORDER BY peso DESC limit 1;")

        line = cursor.fetchone()

        return Ox(identifier=line[0], breed=line[1], weight=line[2])


def get_leaner() -> Ox:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT identificador, raca, peso FROM boi ORDER BY peso ASC limit 1;")

        line = cursor.fetchone()

        return Ox(identifier=line[0], breed=line[1], weight=line[2])


def filter_by_breed(breed) -> list[Ox]:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT identificador, raca, peso FROM boi WHERE raca = ?  ORDER BY identificador ASC;", (breed,)
        )

        return [Ox(identifier=line[0], breed=line[1], weight=line[2]) for line in cursor.fetchall()]
