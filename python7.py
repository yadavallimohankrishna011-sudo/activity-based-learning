# Examination Answer Evaluation

answer_key = ["A", "B", "C", "D", "A"]

students = {
    "Student 1": ["A", "B", "C", "A", "A"],
    "Student 2": ["A", "C", "C", "", "B"],
    "Student 3": ["B", "B", "", "D", "A"]
}

for name, answers in students.items():

    correct = 0
    incorrect = 0
    unanswered = 0

    for i in range(5):

        if answers[i] == "":
            unanswered += 1

        elif answers[i] == answer_key[i]:
            correct += 1

        else:
            incorrect += 1

    marks = (correct * 2) - (incorrect * 0.5)

    print("Student:", name)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Unanswered:", unanswered)
    print("Total Marks:", marks)
    print("-------------------")