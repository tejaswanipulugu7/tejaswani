# Define a list of questions and their corresponding answers
questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "answer": "Blue whale"
    }
]

def present_questions(questions):
    for idx, q in enumerate(questions, start=1):
        print(f"Question {idx}: {q['question']}")
        user_answer = input("Your answer: ")

        # Check if the user's answer matches the correct answer
        if user_answer.lower() == q['answer'].lower():
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is: {q['answer']}")

if __name__ == "__main__":
    print("Welcome to the Quiz App!\n")
    present_questions(questions)
