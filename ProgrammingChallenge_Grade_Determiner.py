# 1. For this exercise, start by creating a variable and assigning that variable a student's score as an integer using input().
grade = int(input("Enter the student's score: "))

# 2. Then, using nested if and else statements and the following set of rules, determine and then display the
# student's grade along with their score using print().
if grade >= 90:
    print("The student will receive an A grade.")
else:
    if grade >= 80:
        print("The student will receive a B grade.")
    else:
        if grade >= 70:
            print("The student will receive a C grade.")
        else:
            if grade >= 60:
                print("The student will receive a D grade.")
            else:
                print("The student will receive an F grade.")