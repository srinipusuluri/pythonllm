import random
import matplotlib.pyplot as plt

# Questions for each section
variable_questions = [
    {"question": "What is a valid variable name?", "options": ["1var", "var_1", "var-1", "1_var"], "answer": "var_1"},
    {"question": "Which of these is not a keyword in Python?", "options": ["if", "else", "elif", "loop"], "answer": "loop"},
    {"question": "Which of these is a valid assignment in Python?", "options": ["x = 5", "5 = x", "int x = 5", "let x = 5"], "answer": "x = 5"},
    {"question": "Which symbol is used to start a comment in Python?", "options": ["#", "//", "/*", "--"], "answer": "#"},
    {"question": "Which of these is not a valid variable name?", "options": ["_var", "var1", "1var", "var_1"], "answer": "1var"}
]

data_type_questions = [
    {"question": "Which of these is a list?", "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "\"1, 2, 3\""], "answer": "[1, 2, 3]"},
    {"question": "What is the type of variable: x = 5?", "options": ["int", "str", "float", "bool"], "answer": "int"},
    {"question": "Which of these is a dictionary?", "options": ["[1, 2, 3]", "{'a': 1, 'b': 2}", "(1, 2, 3)", "{1, 2, 3}"], "answer": "{'a': 1, 'b': 2}"},
    {"question": "What is the type of variable: x = 'Hello'?", "options": ["int", "str", "float", "bool"], "answer": "str"},
    {"question": "Which of these is a tuple?", "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "\"1, 2, 3\""], "answer": "(1, 2, 3)"}
]

operator_questions = [
    {"question": "What is the result of 5 + 3?", "options": ["8", "53", "15", "None of the above"], "answer": "8"},
    {"question": "What is the result of 10 % 3?", "options": ["1", "3", "10", "0"], "answer": "1"},
    {"question": "What is the result of 4 ** 2?", "options": ["16", "8", "4", "2"], "answer": "16"},
    {"question": "What is the result of 9 // 2?", "options": ["4", "4.5", "5", "None of the above"], "answer": "4"},
    {"question": "Which operator is used for logical 'and'?", "options": ["&&", "&", "and", "&&&"], "answer": "and"}
]

def ask_questions(questions):
    correct_answers = 0
    for q in questions:
        try:
            print(q["question"])
            for idx, option in enumerate(q["options"], 1):
                print(f"{idx}. {option}")
            
            while True:
                try:
                    answer = int(input("Choose the correct option (1/2/3/4): "))
                    if answer < 1 or answer > 4:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")
            
            if q["options"][answer - 1] == q["answer"]:
                correct_answers += 1
            print()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Skipping this question.\n")
    return correct_answers

# Main quiz function
def quiz():
    try:
        print("Variables Section:")
        variables_correct = ask_questions(variable_questions)
        print(f"Correct Answers in Variables Section: {variables_correct}/5\n")
        
        print("Data Types Section:")
        data_types_correct = ask_questions(data_type_questions)
        print(f"Correct Answers in Data Types Section: {data_types_correct}/5\n")
        
        print("Operators Section:")
        operators_correct = ask_questions(operator_questions)
        print(f"Correct Answers in Operators Section: {operators_correct}/5\n")
        
        # Calculate percentages
        sections = ['Variables', 'Data Types', 'Operators']
        correct_answers = [variables_correct, data_types_correct, operators_correct]
        total_questions = 5
        percentages = [(correct / total_questions) * 100 for correct in correct_answers]
        
        # Generate the graph
        plt.bar(sections, percentages, color=['blue', 'orange', 'green'])
        plt.xlabel('Sections')
        plt.ylabel('Percentage Correct')
        plt.title('Quiz Results')
        plt.ylim(0, 100)
        plt.show()
        plt.close()
    except Exception as e:
        print(f"An error occurred during the quiz: {e}")

# Run the quiz
quiz()
