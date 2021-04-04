"""Main application."""

from dal import create, delete, filter_by_breed, get, get_fatter, get_leaner, list_all, update
from view import MENU, print_ox


def menu() -> None:
    """Show menu and ask user action."""
    option = -1

    while option != 9:
        option = int(input(MENU))
        if option == 1:
            identifier = int(input("Informe o número de identificação: "))
            breed = input("Informe a raça: ")
            weight = float(input("Informe o peso: "))

            create(identifier=identifier, breed=breed, weight=weight)

            print("\nBoi inserido com sucesso!\n\n")

        if option == 2:
            identifier = int(input("Informe o número de identificação: "))
            print_ox(get(identifier=identifier))

        elif option == 3:
            print_ox(*list_all())

        elif option == 4:
            print_ox(get_fatter())

        elif option == 5:
            print_ox(get_leaner())

        elif option == 6:
            breed = input("Informe a raça: ")
            print_ox(filter_by_breed(breed=breed))

        elif option == 7:
            identifier = int(input("Informe o número de identificação: "))
            delete(identifier=identifier)

            print("\nBoi removido com sucesso!\n\n")

        elif option == 8:
            identifier = int(input("Informe o número de identificação: "))
            breed = input("Informe a raça: ")
            weight = float(input("Informe o peso: "))

            update(identifier=identifier, breed=breed, weight=weight)

            print("\nBoi atualizado com sucesso!\n\n")

    print("\nAté a próxima!!!")


if __name__ == "__main__":
    menu()
