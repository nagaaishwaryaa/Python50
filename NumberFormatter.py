def format_indian_number(number):
    number = str(number).strip()

    # Remove any leading 0 or +91
    if number.startswith("+91"):
        number = number[3:]
    elif number.startswith("91") and len(number) == 12:
        number = number[2:]
    elif number.startswith("0"):
        number = number[1:]

    if len(number) == 10 and number.isdigit():
        return f"+91 {number[:5]} {number[5:]}"
    else:
        return "Invalid input. Please enter a valid Indian 10-digit mobile number."

# Example usage
user_input = input("Enter an Indian mobile number: ")
formatted = format_indian_number(user_input)
print("Formatted Number:", formatted)
