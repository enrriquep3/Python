#This program convert grades from numbers (0-100) to A,B,C,D,F grades.

grade = int(input("enter your grade:\n"))
if grade >= 100:
    print("You Grade is: A. Congratulations You got over 100%! you're genius!")
elif grade >= 90:
    print("You Grade is: A. Congratulations!")
elif grade >= 80:
    print("You Grade is: B. Congratulations!")
elif grade >= 70:
    print("You Grade is: C. You struggle with this course")
elif grade >= 60:
    print("You Grade is: D. You struggle with this course")
else:
    print("You Grade is: F. You Failed this course")
