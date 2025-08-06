s = set() # Initialize an empty set
s.add(20) # Add an integer to the set 
s.add(20.0) # Add a float to the set
s.add('20') # length of s after these operations? # this is string
print(len(s))  # Output: 2, because 20 and 20.0 are considered the same number, and '20' is a different type.
print(s)  # it will print the set
print("this will print 20 as integer one time because in set 20.0 and 20 are considered same")
print("if you fill 30.0 and 20 then it will give you 3 length because 30.0 is different from 20 and 20.0")
print("remember that 20.0 and 20 are same and print only one time while \"20\"is sting in set")