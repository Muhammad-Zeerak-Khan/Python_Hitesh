class CustomException(Exception):
    pass


def brew_chai(flavor: str, cups: int) -> None:
    menu: dict[str, int] = {"masala": 5, "ginger": 3}
    try:
        if flavor not in ["ginger", "masala"]:
            raise CustomException("Flavor not available!")

        if not isinstance(cups, int):
            raise TypeError("Invalid entry of cups")
        total: int = menu[flavor] * cups
        print(f"Your bill for {cups} cups for {flavor} chai is : {total}")
    except Exception as e:
        print(f"Exception: {e}")

    finally:
        print("Thanks for the visit! See you again 😊")


if __name__ == "__main__":
    brew_chai("mint", 2)
    brew_chai("ginger", "three")
    brew_chai("masala", 3)
