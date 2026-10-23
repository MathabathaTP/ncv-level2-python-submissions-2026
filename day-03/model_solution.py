

print("==========================================")
print("     STUDENT ADMISSION SYSTEM - 2027")
print("==========================================")

another_student = "Y"

while another_student == "Y":

   
    full_name = input("\nEnter full name: ")
    id_number = input("Enter ID/Student number: ")

    print("\nAvailable Programmes")
    print("1. Robotics")
    print("2. Mechatronics")
    print("3. Aircraft Maintenance")
    print("4. Aviation")

    programme_choice = int(input("\nChoose a programme (1-4): "))


    if programme_choice == 1:
        programme = "Robotics"
        required_points = 8

    elif programme_choice == 2:
        programme = "Mechatronics"
        required_points = 10

    elif programme_choice == 3:
        programme = "Aircraft Maintenance"
        required_points = 12

    elif programme_choice == 4:
        programme = "Aviation"
        required_points = 14

    else:
        print("ERROR: Programme must be between 1 and 4.")
        continue

   
    maths_mark = int(input("Enter Mathematics mark (0-100): "))
    science_mark = int(input("Enter Physical Sciences mark (0-100): "))

  
    if maths_mark < 0 or maths_mark > 100:
        print("ERROR: Mathematics mark must be between 0 and 100.")
        continue

    if science_mark < 0 or science_mark > 100:
        print("ERROR: Physical Sciences mark must be between 0 and 100.")
        continue

  
    if maths_mark <= 39:
        maths_points = 1
    elif maths_mark <= 49:
        maths_points = 2
    elif maths_mark <= 69:
        maths_points = 4
    elif maths_mark <= 89:
        maths_points = 6
    else:
        maths_points = 7

 
    if science_mark <= 39:
        science_points = 1
    elif science_mark <= 49:
        science_points = 2
    elif science_mark <= 69:
        science_points = 4
    elif science_mark <= 89:
        science_points = 6
    else:
        science_points = 7


    total_points = maths_points + science_points


    if total_points >= required_points:
        admission_status = "ACCEPTED"
    else:
        admission_status = "NOT ACCEPTED"


    print("\n==========================================")
    print("          STUDENT ADMISSION RESULT")
    print("==========================================")
    print("Full Name          :", full_name)
    print("ID/Student Number  :", id_number)
    print("Programme          :", programme)
    print("------------------------------------------")
    print("Mathematics        :", maths_mark, "%")
    print("Maths Points       :", maths_points)
    print("Physical Sciences  :", science_mark, "%")
    print("Science Points     :", science_points)
    print("------------------------------------------")
    print("Total Points       :", total_points)
    print("Required Points    :", required_points)
    print("Admission Status   :", admission_status)
    print("==========================================")

    another_student = input(
        "\nDo you want to capture another student? (Y/N): "
    ).upper()

print("\nThank you for using the Student Admission System.")
print("Program ended.")