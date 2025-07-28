def is_positive(number):
    """Check if the number is positive."""
    return number > 0

def is_even(number):
    """Check if the number is even."""
    return number % 2 == 0

def is_prime(number):
    """Check if the number is prime."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Example usage:
num = int(input("Enter a number: "))

print(f"Is {num} positive? {'Yes' if is_positive(num) else 'No'}")
print(f"Is {num} even? {'Yes' if is_even(num) else 'No'}")
print(f"Is {num} prime? {'Yes' if is_prime(num) else 'No'}")
