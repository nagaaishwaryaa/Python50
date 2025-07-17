import argparse
from collections import Counter

def count_vowels(text):
    vowels = set('aeiouAEIOU')
    vowel_counter = Counter()

    total_chars = len(text)
    vowel_count = 0

    for char in text:
        if char in vowels:
            vowel_counter[char.lower()] += 1
            vowel_count += 1

    # Calculate vowel percentage
    percentage = (vowel_count / total_chars * 100) if total_chars > 0 else 0

    # Find most frequent vowel
    most_common = vowel_counter.most_common(1)
    most_frequent = most_common[0] if most_common else ("None", 0)

    return vowel_count, percentage, vowel_counter, most_frequent


def main():
    parser = argparse.ArgumentParser(description="Count vowels in a word or file.")
    parser.add_argument("-f", "--file", help="Path to a text file", type=str)
    parser.add_argument("-t", "--text", help="Text input directly", type=str)

    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as file:
                content = file.read()
        except FileNotFoundError:
            print("File not found. Please check the path.")
            return
    elif args.text:
        content = args.text
    else:
        content = input("Enter a word or sentence: ")

    total, percent, breakdown, most_frequent = count_vowels(content)

    print("\n📊 Vowel Analysis Result")
    print("-" * 30)
    print(f"Total characters: {len(content)}")
    print(f"Total vowels: {total}")
    print(f"Vowel percentage: {percent:.2f}%")
    print("Breakdown by vowel:")
    for vowel in "aeiou":
        print(f"  {vowel.upper()}: {breakdown.get(vowel, 0)}")
    print(f"Most frequent vowel: {most_frequent[0].upper()} ({most_frequent[1]} times)")


if __name__ == "__main__":
    main()
