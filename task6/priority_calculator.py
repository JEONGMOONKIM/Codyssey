def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def main():
    enter_expression = input("Enter expression: ").split()

    if len(enter_expression) % 2 == 0:
        print("Invalid input.")
        return
    
    for i in range(len(enter_expression)):
        if i % 2 == 0:
            try:
                float(enter_expression[i])
            except ValueError:
                print("Invalid input.")
                return
        else:
            if enter_expression[i] not in ("+", "-", "*", "/"):
                print("Invalid input.")
                return
            
    number = [float(x) for x in enter_expression[0::2]]
    operator = enter_expression[1::2]


    while "*" in operator or "/" in operator:
        for i in range(len(operator)):
            if operator[i] == "*" or operator[i] == "/":
                if operator[i] == "*":
                    number[i] = multiply(number[i], number[i+1])
                elif operator[i] == "/":
                    if number[i+1] == 0:
                        print("Error: Division by zero.")
                        return
                    number[i] = divide(number[i], number[i+1])
                del number[i+1]
                del operator[i]
                break

    while "+" in operator or "-" in operator:
        for i in range(len(operator)):
            if operator[i] == "+":
                number[i] = add(number[i], number[i+1])
            elif operator[i] == "-":
                number[i] = subtract(number[i], number[i+1])
            del number[i+1]
            del operator[i]
            break
    
    print(f"Result: {number[0]}")


if __name__ == "__main__":
    main()   