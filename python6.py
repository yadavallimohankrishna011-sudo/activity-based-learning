# Campus Registration Identifier Analyzer

students = [
    "24CSE101",
    "25ECE102",
    "24MECH103",
    "23CSE104",
    "25ABC105"
]

for student in students:

    if len(student) == 8 and student[:2].isdigit():

        year = student[:2]
        branch = student[2:5]
        number = student[5:]

        print("Student ID:", student)
        print("Admission Year:", "20" + year)
        print("Branch:", branch)
        print("Roll Number:", number)

        if branch == "CSE":
            print("Department: Computer Science")
        elif branch == "ECE":
            print("Department: Electronics")
        elif branch == "MEC":
            print("Department: Mechanical")
        else:
            print("Department: Unknown")

    else:
        print("Invalid Student ID:", student)

    print("-------------------")