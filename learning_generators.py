# Generator
# def serve_chai():
#     yield "Masala Chai"
#     yield "Elaichi Chai"
#     yield "Ginger Chai"


# stall = serve_chai()
# for chai in stall:
#     print(chai)


# Infinite generators
# def infinite_chai():
#     count = 0
#     while True:
#         yield f"Refill #{count}"
#         count += 1


# refil = infinite_chai()

# for _ in range(3):
#     print(f"Refill from first client : {next(refil)}")

# print("-" * 20)
# for _ in range(5):
#     print(f"Refill from second client : {next(refil)}")


# Practical Example of infinite generator
# def chai_customer():
#     print("Welcome to the chai club! So, what's it gonna be ?")
#     order = yield
#     while True:
#         print(f"Preparing the order for : {order}")
#         order = yield
#         print(f"Order for : {order} completed!")


# stall = chai_customer()
# next(stall)  # Start the generator

# stall.send("Masala Chai")
# stall.send("Ginger Tea")


# Yield from syntax
def local_chai():
    yield "Masala Chai from the local stall"
    yield "Doodh Patti from the local stall"


def imported_chai():
    yield "Ice Tea from the imported stall"
    yield "Ginger Tea from the imported stall"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)
