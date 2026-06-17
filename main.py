#student mangment system
student = []

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("Choose from menu")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name of the student: ")
        marks = float(input("Enter student's marks: "))

        if marks > 75:
            result = "DISTINCTION"
        elif marks >= 35:
            result = "PASS"
        else:
            result = "FAIL"

        student.append({
            "name": name,
            "marks": marks,
            "result": result
        })

        print("<<Added Successfully>>")

    elif choice == 2:
        if len(student) == 0:
            print("No student found.")
        else:
            print("\nStudent List:")
            for i, student_s in enumerate(student, start=1):
                print(f"{i},{student}")

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("INVALID CHOICE")