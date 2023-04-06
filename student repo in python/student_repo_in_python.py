import json



print("---------Scripting and Programming - Applications -C867---------------")
print("-----------------------MADE WITH PYTHON BY <YOUR NAME> -------------------")
print("--------------------STUDENT ID:  99999999 ---------------------------")
print("\n")




# Load data from JSON file
with open("student_data.json", "r") as file:
    student_roster = json.load(file)

# Function to add a student
def add_student():
    id = input("Enter student ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email address: ")
    age = int(input("Enter age: "))
    courses = input("Enter student's courses separated by commas: ").split(",")
    degree_program = input("Enter degree program: ")
    new_student = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "courses": courses,
        "degree_program": degree_program
    }
    student_roster["students"].append(new_student)
    print("Student added successfully.")

# Function to remove a student
def remove_student():
    id = input("Enter student ID: ")
    for student in student_roster["students"]:
        if student["id"] == id:
            student_roster["students"].remove(student)
            print("Student removed successfully.")
            return
    print("Student not found.")

# Function to print information for a single student
def print_student():
    id = input("Enter student ID: ")
    for student in student_roster["students"]:
        if student["id"] == id:
            print("Student ID:", student["id"])
            print("First name:", student["first_name"])
            print("Last name:", student["last_name"])
            print("Email address:", student["email"])
            print("Age:", student["age"])
            print("Courses:", student["courses"])
            print("Degree program:", student["degree_program"])
            return
    print("Student not found.")

# Function to print information for all students
def print_all_students():
    for student in student_roster["students"]:
        print("Student ID:", student["id"])
        print("First name:", student["first_name"])
        print("Last name:", student["last_name"])
        print("Email address:", student["email"])
        print("Age:", student["age"])
        print("Courses:", student["courses"])
        print("Degree program:", student["degree_program"])
        print()

# Save data back to JSON file
def save_data():
    with open("student_data.json", "w") as file:
        json.dump(student_roster, file)
        print("Data saved successfully.")

# Main function
def main():
    while True:
        print("Student Roster Management System")
        print("1. Add student")
        print("2. Remove student")
        print("3. Print student information")
        print("4. Print information for all students")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            print_student()
        elif choice == "4":
            print_all_students()
        elif choice == "5":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
