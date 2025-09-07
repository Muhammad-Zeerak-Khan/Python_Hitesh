essential_spices: set[str] = {"cardamom", "ginger", "cinnamon"}
optional_spices: set[str] = {"cloves", "ginger", "black peppre"}

all_spices: set[str] = essential_spices | optional_spices

print(f"Union of all spices is  : {all_spices}")

common_spices: set[str] = essential_spices & optional_spices
print(f"Common spices : {common_spices}")

only_in_essential: set[str] = essential_spices - optional_spices
print(f"Only in essential spices : {only_in_essential}")

# Membership test
print(f"Is 'cloves' in essential spices : {'cloves' in essential_spices}")


# dictionary udemy exercise
customer = {"name": "John Doe", "age": 32, "city": "New York"}
print(customer)

customer.update({"email": "xyz@abc.com", "phone": 12345})

print(customer)

print(customer["name"])
print(customer["city"])

print("email" in customer.keys())

del customer["age"]
print(customer)

print(customer.keys())
print(customer.values())
print(customer.items())
