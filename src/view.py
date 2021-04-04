"""Methods to show ox data."""

import textwrap

from model import Ox

MENU = textwrap.dedent(
    """\
    Selecione a opção desejada:
    1 - Cadastrar
    2 - Consultar
    3 - Listar
    4 - Obter boi mais gordo
    5 - Obter boi mais magro
    6 - Listar boi por raça
    7 - Excluir
    8 - Alterar
    9 - Sair

    Opção: """
)


def print_ox(*args: Ox) -> None:
    """Print pretty Ox data.

    Parameters
    ----------
    args: Ox instance.
    """
    print("\n\nResultado:\n")

    for ox in args:
        print(
            textwrap.dedent(
                f"""\
            ---------------------------------
            Identificador: {ox.identifier}
            Peso: {ox.weight}
            Raça: {ox.breed}
            ---------------------------------
        """
            )
        )
