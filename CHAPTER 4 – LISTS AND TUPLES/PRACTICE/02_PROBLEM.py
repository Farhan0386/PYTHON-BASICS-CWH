marks=[]   #this empty list will hold the marks of the students

m1=int(input("Enter the marks of  MATHS:")) # first we take inpiut from the user
marks.append(m1)                            # then we add the user value to the list name "marks"
m2=int(input("Enter the marks of ENGLISH:"))
marks.append(m2)
m3=int(input("Enter the marks of the  CHEMISTRY:"))
marks.append(m3)
m4=int(input("Enter the marks of the  PHYSICS:"))
marks.append(m4)
m5=int(input("Enter the marks of the PHYSICAL EDUCATION:"))
marks.append(m5)

print("The marks of the students are: ",  sum(marks),"out of 500")  # this will print the total marks of the students
marks.sort()                                                        # this will sort the marks in ascending order
print("The highest marks are in: ", marks[-1])                      # after sorting, the last element will be the highest marks , we also use  4 instead of -1
print("The lowest marks are in: ", marks[0])                        # after sorting, the first element will be the lowest marks
print("The student got ",sum(marks)/5, "%")                # this will print the percentage of the student by dividing the total marks by 5



