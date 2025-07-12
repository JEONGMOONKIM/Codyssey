def main():
    try:
        base = float(input("Enter number: "))
    except ValueError:
        print("Invalid number input.")
        return

    try:
        exponent = int(input("Enter exponent: "))
    except ValueError:
        print("Invalid exponent input.")
        return

    result = 1
    if exponent == 0:
        result = 1
    elif exponent > 0:
        for _ in range(exponent):
            result *= base
    else:
        for _ in range(-exponent):
            result *= base
        result = 1 / result

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
