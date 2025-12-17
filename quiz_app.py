
import time

QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": ["function", "def", "fun", "define"],
        "answer": 1
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "choices": ["6", "8", "9", "5"],
        "answer": 1
    },
    {
        "question": "Which data type stores multiple values?",
        "choices": ["int", "float", "list", "bool"],
        "answer": 2
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "choices": ["//", "#", "/*", "<!--"],
        "answer": 1
    },
    {
        "question": "Which function takes user input?",
        "choices": ["scan()", "input()", "read()", "get()"],
        "answer": 1
    }
]

def run_quiz():
    print("WELCOME TO QUIZ APPLICATION")
    name = input("Enter your name: ")
    score = 0

    for i, q in enumerate(QUESTIONS, start=1):
        print(f"\nQ{i}. {q['question']}")
        for idx, opt in enumerate(q['choices'], start=1):
            print(f"{idx}. {opt}")
        ans = int(input("Enter your choice: ")) - 1
        if ans == q['answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer")

    print(f"\n{name}, your final score is {score}/{len(QUESTIONS)}")

if __name__ == "__main__":
    run_quiz()
