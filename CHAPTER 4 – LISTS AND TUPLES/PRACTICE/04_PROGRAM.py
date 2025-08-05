list1=[] # this is a list to store the numbers
# this program will take four numbers from the user and store them in a list, then sort the list and print it along with the sum of the numbers

n1=int(input("Enter the first number : ")) #| input the first number ,we typecast it to int because we use arthematic operations on it like sum as we know that input from is always a string until we typecast it|                       
list1.append(n1)
n2=int(input("Enter the second number : "))
list1.append(n2)    
n3=int(input("Enter the third number : "))
list1.append(n3)
n4=int(input("Enter the fourth number : "))
list1.append(n4)
list1.sort() # this will sort the list in ascending order
print("the numbers are ",list1, "sum of the numbers is ", sum(list1)) # this will print the list and the sum of the numbers
# the sum function will return the sum of all the numbers in the list
