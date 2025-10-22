print("This is program for checking whether a Student is passes or fail in Exams.\nYou can provide marks of 3 subjects in this program.")
print()
sub1=float(input("Enter your marks of Maths:"))
print()
sub2=float(input("Enter your marks of English:"))
print()
sub3=float(input("Enter your marks in Science:"))
print()
if  0<=sub1<=100:
    if sub1<=33:
        print("Student is fail in Maths")
else:
    print("Invalid Marks")
if  0<=sub2<=100:
    if sub2<=33:
        print("Student is fail in English")
else:
    print("Invalid Marks")
if  0<=sub3<=100:
    if sub3<=33:
        print("Student is fail in Science")
else:
    print("Invalid Marks")
average_sum=(sub1+sub2+sub3)/3
print()
print(f"Average marks of Student in 3 subjects is {average_sum}")
print()
if average_sum>=40:
    print(f"Student is passed in exams with {average_sum}%") 
else:print(f"Student is failed with {average_sum}%")

