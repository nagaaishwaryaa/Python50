def find_largest(numbers):
    if not numbers:
        return None  # Handle empty list

    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

def main():
    # Example list of numbers
    numbers = []

    count = int(input("How many numbers do you want to enter? "))
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    largest = find_largest(numbers)

    if largest is not None:
        print(f"\nThe largest number in the list is: {largest}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()
