while True:
    print("\n----- REPORT CARD GENERATOR -----")
    print("1. Generate Report Card")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        no_of_subject = int(input("Enter Number of Subjects: "))
        subjects = []
        marks = []
        for i in range(no_of_subject):
            subject_name = input(f"Enter Subject {i + 1} Name: ")
            subject_marks = int(input(f"Enter {subject_name} Marks: "))
            subjects.append(subject_name)
            marks.append(subject_marks)
        invalid_marks = False
        for mark in marks:
            if mark < 0 or mark > 100:
                invalid_marks = True
                break

        if invalid_marks:
            print("Marks should be from 0 to 100.")
            continue
        total = sum(marks)
        pct = total / no_of_subject

        if pct >= 90:
            grade = "Outstanding!"
        elif pct >= 80:
            grade = "Excellent!"
        elif pct >= 70:
            grade = "Very Good!"
        elif pct >= 60:
            grade = "Good!"
        elif pct >= 50:
            grade = "Needs Improvement"
        else:
            grade = "Fail"

        result = "PASS"
        for mark in marks:
            if mark < 33:
                result = "FAIL"
                break
        print("\n---------- REPORT CARD ----------")
        print("Student Name :", name)
        print("Roll Number  :", roll)
        print("---------------------------------")
        print(f"Total       : {total}/{no_of_subject * 100}")
        print(f"Percentage  : {pct:.2f}%")
        print(f"Grade       : {grade}")
        print(f"Result      : {result}")
        print("---------------------------------")
    elif choice == 2:
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Please try again.")