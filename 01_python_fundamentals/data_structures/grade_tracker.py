grades = {}

while True:
    print("\n--- STUDENT GRADE TRACKER ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Class average")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("student name: "
                     )
        score = float(input("grade: "))
        grades[name] = score
        print("student added.")
    elif choice == "2":
        if not grades:
            print("No students yet.")
        else
        for name, score in grades.tems():
            print(f"{name}: {score}")
    elif choice == "3":
        if not grades:
            print("no grades to calculate.")
        else:
            total = sum(grades.values())
            average = total / len(grades)
            print(f"Class average: {average:.2f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("invalid option")
