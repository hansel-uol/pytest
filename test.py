def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def main():
    num1 = 10
    num2 = 5
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

    result = multiply_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is {result}")


if __name__ == "__main__":
    main()
