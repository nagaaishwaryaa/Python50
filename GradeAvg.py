def get_scores():
    scores = []
    for i in range(1, 6):
        while True:
            try:
                score = float(input(f"Enter score {i} (out of 100): "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return scores

def calculate_average(scores):
    return sum(scores) / len(scores)

def check_pass(avg_score):
    return avg_score >= 40

def main():
    print("Enter the 5 test scores:")
    scores = get_scores()
    average = calculate_average(scores)
    status = "PASS" if check_pass(average) else "FAIL"
    
    print(f"\nAverage Score: {average:.2f}")
    print(f"Result: {status}")

if __name__ == "__main__":
    main()
