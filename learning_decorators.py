from functools import wraps


def my_decorator(input_function):
    @wraps(input_function)
    def wrapper(*args, **kwargs):
        print(f"Before running the function {input_function.__name__}()")
        input_function(*args, **kwargs)
        print(f"After running the function {input_function.__name__}()")

    return wrapper


@my_decorator
def greet(age, name="Default Name"):
    print(f"Hello from the greetings function having the name :{name}")


print(greet(age=15, name="ZK"))
print(greet.__name__)
