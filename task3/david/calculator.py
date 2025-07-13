def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b


def main():
    # try:
    #     a = int(input("Enter num1: "))
    # except ValueError:
    #     print("Invalid number input.")
    #     return

    # try:
    #     b = int(input("Enter num2: "))
    # except ValueError:
    #     print("Invalid number input.")
    #     return

    # operator = input("Enter operator: ")

    # if operator == "+":
    #     result = add(a, b)
    # elif operator == "-":
    #     result = subtract(a, b)
    # elif operator == "*":
    #     result = multiply(a, b)
    # elif operator == "/":
    #     result = divide(a, b)
    #     if result is None:
    #         return
    # else:
    #     print("Invalid operator.")
    #     return

    # print(f"Result: <{result}>")

    enter_expression = input("Enter expression: ")

    try:
        parts = enter_expression.strip().split()
        # parts = enter_expression.strip().split(maxsplit=2)
        if len(parts) != 3:
            print("Invalid expression.")
            return

        a_str, operator, b_str = parts
        a = int(a_str)
        b = int(b_str)

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
            if result is None:
                return
        else:
            print("Invalid expression.")
            return

        print(f"Result: <{result}>")
    
    except ValueError:
        print("Invalid expression.")

if __name__ == "__main__":
    main()