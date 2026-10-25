# Grade calculator

marks = 180

if marks >= 101:
    print("Invalid marks. Please enter a value between 0 and 100.")
    exit()


if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)