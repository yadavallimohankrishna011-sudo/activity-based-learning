# Student Timetable Conflict Detection

timetable = [
    ("Python", "09:00", "10:00", "Room A"),
    ("Maths", "10:00", "11:00", "Room B"),
    ("Physics", "09:30", "10:30", "Room C"),
    ("English", "11:00", "12:00", "Room A")
]

unavailable_rooms = ["Room C"]

for i in range(len(timetable)):
    subject, start, end, room = timetable[i]

    if room in unavailable_rooms:
        print(subject, "- Room Unavailable")

    else:
        print(subject, "- Room Available")

    for j in range(i + 1, len(timetable)):
        subject2, start2, end2, room2 = timetable[j]

        if start < end2 and start2 < end:
            print("Time Conflict:", subject, "and", subject2)

print("\nTimetable Validation Completed")