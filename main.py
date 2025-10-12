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
    # print(
    #     "This is a shorter line replacing the long line that exceeded the"
    #     " recommended maximum line length of 79 characters."
    # )
    print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 "
          "21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 "
          "36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54") 


if __name__ == "__main__":
    my_function(10, 5)
    example = ExampleClass(42)
    example.show_value()
    long_line_function()
# This script demonstrates a clean and PEP8 compliant Python code structure.
