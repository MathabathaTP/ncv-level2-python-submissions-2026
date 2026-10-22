mark_str = input("insert your mark or -1 to stop: ")


if mark_str.isdigit():
    mark = int(mark_str)
    print("your entered mark is",mark)
    if mark >= 0 and mark <= 100 : 
        if mark >= 80:
            print("Outstanding")
        elif mark >= 70:
            print("Highly competent")
        elif mark >= 50:
            print("Competent")
        elif mark >= 40:
            print("Not yet competent")
        elif mark >= 0:
            print("Not achieved")
    else :
        print("invalid mark  :")
else :
    print("invalid entry  :")
