def main():
    numbers = list(map(float, input("Enter numbers: ").split()))
    min_val = numbers[0]
    max_val = numbers[0]

    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    print(f"Min: {min_val} Max: {max_val}")

if __name__ == "__main__":
    main()
