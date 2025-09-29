from typing import Self


class ChaiOrder:
    def __init__(self, tea_type, sweetness, size) -> None:
        self.tea_type: str = tea_type
        self.sweetness: str = sweetness
        self.size: str = size

    @classmethod
    def from_dict(cls, order_data) -> Self:
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string: str) -> Self:
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)


# From Dict
order1: ChaiOrder = ChaiOrder.from_dict(
    {"tea_type": "masala", "sweetness": "medium", "size": "small"}
)
# From String
order2: ChaiOrder = ChaiOrder.from_string("Ginger-Low-Large")

# Usual Object
order3: ChaiOrder = ChaiOrder("Green", "Low", "Medium")

print(f"Order1 : {order1.__dict__}")
print(f"Order2 : {order2.__dict__}")
print(f"Order3 : {order3.__dict__}")
