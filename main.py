# Clean and PEP8 compliant version of the script


def my_function(a, b):
    if a > b:
        print("A is greater than B")
    else:
        print("B is greater or equal to A")


class ExampleClass:

    def __init__(self, value):
        self.value = value

    def show_value(self):
        print("The value is:", self.value)


def long_line_function():
    print(
        "This is a shorter line replacing the long line that exceeded the"
        " recommended maximum line length of 79 characters."
    )


if __name__ == "__main__":
    my_function(10, 5)
    example = ExampleClass(42)
    example.show_value()
    long_line_function()
# This script demonstrates a clean and PEP8 compliant Python code structure.
