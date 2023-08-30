print("Welcome to the grade calculator.")

CDISum = int(input("Please enter the sum of your Cryptography Discussions and DI Assignment Grades, up to 700: "))

LabSum = int(input("Please enter the sum of all your lab grades, up to 900: "))

QuizSum = int(input("Please enter the sum of all your quiz grades, up to 800: "))

Midterm = int(input("Please enter your midterm grade: "))

Final = int(input("Pleae enter your final exam grade: "))

CDIGrade = (CDISum/7)*.10
LabGrade = (LabSum/9)* .20
QuizGrade = (QuizSum/8) * .20
MidtermGrade = Midterm * .25
ExamGrade = Final * .25

FinalGrade = CDIGrade + LabGrade + QuizGrade + MidtermGrade + ExamGrade

print("Your final grade is: ")
print(FinalGrade)


             
