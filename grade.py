grade = int(input("Enter your grade: "))
match grade:
    case grade if grade >= 90:
        print("A")
    case grade if grade >= 80 and grade < 90:
        print("B")
    case grade if grade >= 70 and grade < 80:
        print("C")
    case grade if grade >= 60 and grade < 70:
        print("D")
