import pandas as pd
import matplotlib.pyplot as plt
import math

# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to find the highest grade
def find_highest_grade(grades):
    return max(grades)

# Function to find the lowest grade
def find_lowest_grade(grades):
    return min(grades)

# Function to add a new student and grade
def add_student(students, grades):
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {name}: ").strip())
            if 0 <= grade <= 100:
                students.append(name)
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid grade.")

# Function to print a summary report
def print_summary(students, grades):
    if not students:
        print("No student data available.")
        return

    # Calculate average, highest, and lowest grades
    average_grade = calculate_average(grades)
    highest_grade = find_highest_grade(grades)
    lowest_grade = find_lowest_grade(grades)

    # Print the results
    print("\nSummary Report")
    print("-" * 20)
    print(f"Total Students: {len(students)}")
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Highest Grade: {highest_grade} (by {students[grades.index(highest_grade)]})")
    print(f"Lowest Grade: {lowest_grade} (by {students[grades.index(lowest_grade)]})")

# Main function to run the program
def main():
    # Define the students and their grades
    students = ["Alice", "Bob", "Charlie", "David", "Eva"]
    grades = [85, 92, 78, 90, 88]

    # Add new students and their grades
    add_student(students, grades)

    # Print summary report
    print_summary(students, grades)

    # Create a DataFrame to store student names and grades
    df = pd.DataFrame({
        "Student": students,
        "Grade": grades
    })

    # Plot the grades as a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(df["Student"], df["Grade"], color='skyblue')
    plt.xlabel("Students")
    plt.ylabel("Grades")
    plt.title("Student Grades")
    plt.ylim(0, 100)  # Set the limit for y-axis from 0 to 100
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
