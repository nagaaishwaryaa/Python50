def calculate_sum_and_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []

            for line in file:
                for part in line.split():
                    if part.strip().isdigit():
                        numbers.append(int(part.strip()))

            if numbers:
                total_sum = sum(numbers)
                average = total_sum / len(numbers)
                print(f"Numbers: {numbers}")
                print(f"Sum: {total_sum}")
                print(f"Average: {average:.2f}")
            else:
                print("No numbers found in the file.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage
filename = input("Enter the file name: ")
calculate_sum_and_average(filename)
