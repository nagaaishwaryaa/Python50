def extract_initials_with_dots(full_name):
    # Remove extra spaces and split the full name
    words = full_name.strip().split()
    # Extract the first letter of each word, capitalize it, and join with dots
    initials = '.'.join(word[0].upper() for word in words if word) + '.'
    return initials

# Example usage
name = input("Enter your full name: ")
print("Initials with dots:", extract_initials_with_dots(name))
