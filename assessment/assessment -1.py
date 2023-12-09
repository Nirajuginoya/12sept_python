import random

class QuizGame:
    def __init__(self):
        self.questions = {}

    def display_menu(self):
        print("\n===== Quiz Game Console Application =====")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Play Game")
        print("5. Exit")

    def add_question(self):
        question_id = input("Enter question ID: ")
        question_text = input("Enter the question: ")
        options = input("Enter options separated by commas: ").split(',')
        correct_answer = input("Enter correct answer: ")

        self.questions[question_id] = {
            'question': question_text,
            'options': options,
            'correct_answer': correct_answer
        }

        print("Question added successfully.")

    def view_questions(self):
        print("\n===== Questions =====")
        for question_id, details in self.questions.items():
            print(f"{question_id}. {details['question']}")
            print(f"Options: {', '.join(details['options'])}")
            print(f"Correct Answer: {details['correct_answer']}\n")

    def delete_question(self):
        question_id = input("Enter question ID to delete: ")
        if question_id in self.questions:
            confirmation = input(f"Are you sure you want to delete question {question_id}? (Y/N): ")
            if confirmation.upper() == 'Y':
                del self.questions[question_id]
                print(f"Question {question_id} deleted successfully.")
            else:
                print("Deletion canceled.")
        else:
            print(f"Question with ID {question_id} not found.")

    def play_game(self):
        if not self.questions:
            print("No questions available. Add questions before playing.")
            return

        print("\n===== Quiz Game =====")
        score = 0
        for _ in range(3):  # Adjust the number of questions to play
            question_id, details = random.choice(list(self.questions.items()))
            print(details['question'])
            for i, option in enumerate(details['options'], 1):
                print(f"{i}. {option}")

            user_answer = input("Your answer (1-{}): ".format(len(details['options'])))
            if user_answer == details['correct_answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! Correct answer: {details['correct_answer']}\n")

        print(f"Your final score: {score}/3")

    def save_data(self):
        with open('quiz_log.txt', 'a') as log_file:
            log_file.write("===== Quiz Log =====\n")
            for question_id, details in self.questions.items():
                log_file.write(f"Question ID: {question_id}\n")
                log_file.write(f"Question: {details['question']}\n")
                log_file.write(f"Options: {', '.join(details['options'])}\n")
                log_file.write(f"Correct Answer: {details['correct_answer']}\n\n")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_question()
            elif choice == '2':
                self.view_questions()
            elif choice == '3':
                self.delete_question()
            elif choice == '4':
                self.play_game()
            elif choice == '5':
                self.save_data()
                print("Thank you for using the Quiz Game Console Application. Exiting...")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.main()