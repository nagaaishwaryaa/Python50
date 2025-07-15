def main():
    names = []

    # Collect 5 names
    for i in range(1, 6):
        name = input(f"Enter name {i}: ")
        names.append(name)

    print("\nNames and their lengths:")
    for name in names:
        print(f"{name} (Length: {len(name)})")

if __name__ == "__main__":
    main()
