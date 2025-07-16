def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): #assert 사용해서도 작성해보기. (except ZeroDivisionError: 삽입)
    if b == 0:
        print("Error: Division by zero.")
        return None
    else:
        return a / b


def first_calculator():

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
        print("Invalid operator.")
        return

    print(f"Result: <{result}>")
    

def second_calculator():
    enter_expression = input("Enter expression: ")

    try:
        parts = enter_expression.split() #strip() 필요없음.
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
        
def main():
    mode = input("Press the number(1 or 2): ")
    if mode == "1":
        first_calculator()
    elif mode == "2":
        second_calculator()
    else:
        print("Invalid expression.")

if __name__ == "__main__":
    main()