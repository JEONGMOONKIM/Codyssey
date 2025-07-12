def main():
    try:
        a = int(input("Enter num1: "))
    except ValueError:
        print("Invalid number input.")
        return

    try:
        b = int(input("Enter num2: "))
    except ValueError:
        print("Invalid number input.")
        return

    operator = input("Enter operator: ")

    if operator not in {"+", "-", "*", "/"}:
        print("Invalid operator.")
        return

    try:
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                print("Error: Division by zero.")
                return
            result = a / b

        print(f"Result: &lt;{result}&gt1;")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
