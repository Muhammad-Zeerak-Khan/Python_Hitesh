class Pencil:
    color: str = "black"
    size: str = "medium"


pencil_1: Pencil = Pencil()
print("Attributing before changing.")
print(f"Color of the pencil from the object : {pencil_1.color}")
print(f"Color of the pencil from the class: {Pencil.color}")

pencil_1.color = "brown"
pencil_1.size = "large"
print("Attributing after changing.")
print(f"Color of the pencil from the object : {pencil_1.color}")
print(f"Color of the pencil from the class : {Pencil.color}")

print("Lets delete the color attribute from the pencil_1 instance and then check..")
del pencil_1.color
print("Attributing after deleting the object's color attribute.")
print(f"Color of the pencil from the object : {pencil_1.color}")
print(f"Color of the pencil from the class : {Pencil.color}")

# This shows that after the attribute from an instance/object is deleted,
# The attribute falls back to the original value from the class

# Lets add a new attribute to the object and check the value after deletion
print("Lets add a new attribute to the object and check the value after deletion")
pencil_1.grip: str = "firm"
print(
    f"New grip attribute added to the pencil_1 object, pencil_1.grip : {pencil_1.grip}"
)
del pencil_1.grip
# print(f"Value of attribute pencil_1.grip after deletion: {pencil_1.grip}")
# throws an AttributeError as it has nothing to fall back on.
