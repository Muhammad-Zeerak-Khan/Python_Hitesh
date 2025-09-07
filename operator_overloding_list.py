# from encodings import utf_16
# from operator import itemgetter

# default_list: list[str] = ["chai", "coffee"]

# # print(default_list + ["juice"])
# # print(default_list * 2)

# # raw_spice_data = bytearray(b"Cloves")
# # print(raw_spice_data)
# # default_list.reverse()
# default_list.extend(["water", "milk"])
# print(default_list)


# mystring = "tomato cucumber spinach"
# l = mystring.split()
# # my_string: list[str] = list(mystring)
# # print(my_string)
# # print(type(mystring))
# print(l)
def calculate_delivery_charge(distance: float) -> str:
    # Write your code below this line
    distance = float(input("Provide the delivery distance in Kilometers : "))
    if distance <= 2:
        return "Delivery charge : 0"
    elif distance > 2 and distance <= 5:
        return "Delivey charge: 30"
    elif distance > 5 and distance <= 10:
        return "Delivey charge: 50"
    else:
        return "Delivery not available for your location"


print(calculate_delivery_charge(3))
