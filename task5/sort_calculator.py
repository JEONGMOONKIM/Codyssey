def main():
    try:
        numbers = list(map(float, input("Enter numbers: ").split()))
    except ValueError:
        print("Invalid number input.")
        return
    
    for i in range(len(numbers)):
            j = len(numbers) - i
            for k in range(1,j):
                if numbers[k-1] >= numbers[k]:
                    temp = numbers[k-1]
                    numbers[k-1] = numbers[k]
                    numbers[k] = temp

    formatted = ''.join(f"<{x}>" for x in numbers)
    print(f"Sorted: {formatted}")
    

if __name__ == "__main__":
    main()   