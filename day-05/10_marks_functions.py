def get_marks():
    marks = []
    mark = int(input("Enter mark or -1 to stop: "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark or -1 to stop: "))

    return marks


def print_list_size(marks):
    print(f"Our list has {len(marks)} elements")


def get_sum_of_marks(marks):
    total = 0

    for x in range(len(marks)):
        mark = marks[x]
        total = total + mark

    return total


def calculate_average(marks):
    if len(marks) > 0:
        total = get_sum_of_marks(marks)
        average = total / len(marks)
        print(f"The average mark is {average:.2f}")
    else:
        print("No marks have been captured.")


def determine_highest(marks):
    if len(marks) > 0:
        highest = marks[0]

        for i in range(len(marks)):
            current_mark = marks[i]

            if current_mark > highest:
                highest = current_mark

        print(f"The highest mark is {highest}")
    else:
        print("No marks have been captured.")


# Main program

menu = """
Press 1: Capture marks
Press 2: Check number of marks
Press 3: Calculate average mark
Press 4: Find highest mark
Press -1: Exit
"""

entered_marks = []

print(menu)
choice = int(input("Make your choice: "))

while choice != -1:

    if choice == 1:
        entered_marks = get_marks()
        print("Marks captured:", entered_marks)

    elif choice == 2:
        print_list_size(entered_marks)

    elif choice == 3:
        calculate_average(entered_marks)

    elif choice == 4:
        determine_highest(entered_marks)

    else:
        print("Choice not in the menu.")

    print(menu)
    choice = int(input("Make your choice: "))

print("Program ended.")