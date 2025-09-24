test_list: list[str] = ["First", "Second", "Third"]

# for idx, item in enumerate(test_list, start=1):
#     print(f"{idx} : {item}")

# The 'start' argument lets the counter to start from an arbitrary number
# other than 1. Although it still gets the first element in the iterable i.e.
# at the 0th position of the iterable.


# Exploring Walrus operator

# if (input_string := input("Enter your string: ")) in test_list:
#     print(f"The entered string {input_string} matches")
# else:
#     print(f"The entered string {input_string} does not match. ")

# flavors: list[str] = ["ginger", "lemon", "mint", "masala"]

# print(f"Available flavors : {flavors}")

# while (flavor := input("Enter the flavor: ")).lower() not in flavors:
#     print(f"Flavor {flavor} not available")

# print(f"You choose {flavor} chai. Great Choice!")


# def make_chai(*ingredients, **extras):
#     print(f"The ingredients are : {ingredients}")
#     print(f"The extras are : {extras}")


# make_chai("Cinammon", "Cardamom", milk="yes", sugar="no")
# d = {"one": 1, "two": 2}
# print(len(d))


# def pour_chai(n):
#     print(f"The value of n is : {n}")
#     if n == 0:
#         return "All cups poured!"
#     print(f"Pouring for {n} cups")
#     return pour_chai(n - 1)


# print(pour_chai(4))
#
# chai_types: list[str] = ["light", "heavy", "medium", "heavy"]

# heavy_chai: list[str] = list(filter(lambda chai_type: chai_type == "heavy", chai_types))

# print(heavy_chai)

# l: list[int] = list(range(10))

# m: list[int] = list(map(lambda x: x**2, l))
# print(m)

# recipes: dict[str, list[str]] = {
#     "Masala Chai": ["ginger", "cardamom", "clove"],
#     "Elaichi Chai": ["cardamom", "milk"],
#     "Spicy Chai": ["ginger", "black pepper", "clove"],
# }

# unique_spices: set[str] = {
#     spice.upper() for ingredients in recipes.values() for spice in ingredients
# }
# print(unique_spices)


# Dictionary Comprehension

# tea_prices_inr: dict[str, int] = {"Masala Chai": 100, "Green Tea": 50, "Lemon Tea": 25}

# tea_prices_eur: dict[str, float] = {
#     tea: float(f"{(price / 330):.3f}") for tea, price in tea_prices_inr.items()
# }
# print(f"The tea prices in INR are  : {tea_prices_inr}")
# print(f"The tea prices in EUR are  : {tea_prices_eur}")


# def test_function(*args, **kwargs):
#     print(f"The positional arguments passed are : {args}")
#     print(f"The first argument passed is : {args[0]}")
#     print(f"The second argument passed is : {args[1]}")
#     print(f"The keyword arguments passed are : {kwargs}")


# test_function("Zk", "TK", "Mk", first_kw="first", second_kw="second")


class SmartDevice:
    brand = "HomeTech"

    def __init__(self, device_name, power_status):
        self.device_name = device_name
        self.power_status = power_status
        self.brand = "CustomBrand"

    def get_status(self):
        print(f"{self.device_name} is {self.power_status} - {self.brand}")


AC = SmartDevice(device_name="AC", power_status="ON")
Fan = SmartDevice(device_name="Fan", power_status="OFF")

AC.get_status()
Fan.get_status()
