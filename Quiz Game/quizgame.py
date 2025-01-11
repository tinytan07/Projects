questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Paris", "2. Berlin", "3. Madrid", "4. Rome"],
        "answer": 1,
    },
    {
        "question": "Which programming language is known as the language of AI?",
        "options": ["1. Java", "2. Python", "3. C++", "4. JavaScript"],
        "answer": 2,
    },
    {
        "question": "What is the square root of 64?",
        "options": ["1. 6", "2. 7", "3. 8", "4. 9"],
        "answer": 3,
    },
]

def run_quiz():
    score = 0
    print("\nWelcome to the Quiz Game!")
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        try:
            answer = int(input("Enter your answer (1-4): "))
            if answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
        except ValueError:
            print("Invalid input. Skipping question.")

    print(f"\nYour final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
