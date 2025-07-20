def shift_sentence_by_one(text):
    shifted = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:  # uppercase
                shifted += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            shifted += char  # Keep spaces, punctuation, numbers unchanged
    return shifted

# Example usage
sentence = input("Enter a sentence: ")
result = shift_sentence_by_one(sentence)
print("Shifted sentence:", result)
