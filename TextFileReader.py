def count_lines_and_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            total_words = sum(len(line.split()) for line in lines)

        print(f"Total Lines: {total_lines}")
        print(f"Total Words: {total_words}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage
filename = input("Enter the path to the text file: ")
count_lines_and_words(filename)
