class ChaiUtils:
    @staticmethod
    def raw_ingredients(raw_text: str) -> list[str]:
        return [text.strip() for text in raw_text.split(",")]


if __name__ == "__main__":
    raw_items = " milk, honey, sugar, ginger,    water"

    main_ingredients: list[str] = ChaiUtils.raw_ingredients(raw_items)
    print(f"The main ingredients are : {main_ingredients}")
