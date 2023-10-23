import json
import datetime


# Function to load questions from a file
def load_questions():
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
    except FileNotFoundError:
        questions = {}
    return questions


# Function to save questions to a file
def save_questions(questions):
    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)


# Function to add a new question
def add_question(questions):
    question = input("Enter the question: ")
    options = [input(f"Enter option {i + 1}: ") for i in range(2)]
    correct_option = input("Enter the correct answer: ")


    question_id = len(questions) + 1
    questions[question_id] = {
        "question": question,
        "options": options,
        "correct_option": correct_option
    }

    save_questions(questions)
    print("Question added successfully!")


# Function to view all questions
def view_questions(questions):
    for question_id, question_data in questions.items():
        print(f"\nQuestion {question_id}: {question_data['question']}")
        for i, option in enumerate(question_data["options"]):
            print(f"{i + 1}. {option}")
        print(f"Correct Answer: {question_data['correct_option']}\n")


# Function to delete a question with confirmation
def delete_question(questions):
    view_questions(questions)  # Display available questions for reference
    question_id = input("Enter the question ID to delete: ")

    if question_id in questions:
        print(f"Question {question_id}: {questions[question_id]['question']}")
        confirm = input("Do you want to delete this question? (Y/N): ").strip().lower()

        if confirm == "y":
            del questions[question_id]
            save_questions(questions)
            print("Question deleted successfully!")
        else:
            print("Deletion canceled / Invalid Choice. Question not removed.")
    else:
        print("Question not found. Please enter a valid question ID.")


# Function to display and answer questions
def quiz_cracker(questions):
    score = 0
    total_questions = len(questions)

    for question_id, question_data in questions.items():
        print(f"\nQuestion {question_id}: {question_data['question']}")
        for i, option in enumerate(question_data["options"]):
            print(f"{i + 1}) {option}")

        user_answer = input("Enter your answer: ")

        if user_answer == question_data["correct_option"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['correct_option']}.")

    print(f"\nThank you for taking a quiz\nYou scored {score}/{total_questions}")

    # Log the quiz results
    log_quiz_result(score, total_questions)


# Function to log quiz results
def log_quiz_result(score, total_questions):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_message = f"Quiz taken at {timestamp}. Scored {score}/{total_questions}.\n"

    with open("quiz_log.txt", "a") as log_file:
        log_file.write(result_message)


# Main function for Quiz Master
def quiz_master_menu():
    print("\n\t\t\t\tWELCOME MASTER")
    while True:
        print("\n\t\t\t\tQUIZ MASTER MENU")
        print("\t\t\t-> Add Question (Press 1)")
        print("\t\t\t-> View Questions (Press 2)")
        print("\t\t\t-> Delete Question (Press 3)")
        print("\t\t\t-> Exit (Press 4)")

        choice = input("\nWhich operation you want to perform: ")

        if choice == "1":
            questions = load_questions()
            add_question(questions)
        elif choice == "2":
            questions = load_questions()
            view_questions(questions)
        elif choice == "3":
            questions = load_questions()
            delete_question(questions)
        elif choice == "4":
            print("Exiting the Quiz Master Menu.")
            break
        else:
            print("Invalid choice. Please try again.")


# Main function for Quiz Cracker
def quiz_cracker_menu():
    questions = load_questions()
    if not questions:
        print("No questions available. Quiz Cracker cannot start.")
        return

    print("\n\t\t\t\t\tWELCOME QUIZ CRACKER")
    while True:
        print("\n\t\t\t\t\tQUIZ CRACKER MENU")
        print("\t\t\t\t-> Take quiz (Press 1)")
        print("\t\t\t\t-> Exit (Press 2)")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            quiz_cracker(questions)
        elif choice == "2":
            print("Exiting the Quiz Cracker Menu.")
            break
        else:
            print("Invalid choice. Please try again.")


# Main function
def main():
    print("\t\t\t\t\tWELCOME TO TOPS QUIZ GAMING CHALLENGE")

    while True:
        print("\n\t\t\t\t\tSelect your role:\n")
        print("\t\t\t\t\t\t-> Quiz Master (Press 1)")
        print("\t\t\t\t\t\t-> Quiz Cracker (Press 2)")
        role_choice = input("\nEnter your role: ")

        if role_choice == "1":
            quiz_master_menu()
        elif role_choice == "2":
            quiz_cracker_menu()
        else:
            print("Invalid choice. Please enter 1 for Quiz Master or 2 for Quiz Cracker.")

if __name__ == "_main_":
    main()
