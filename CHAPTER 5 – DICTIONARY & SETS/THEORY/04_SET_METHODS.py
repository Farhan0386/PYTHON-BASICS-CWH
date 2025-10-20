
s = {1,2,4,6,3,2,5,4,2,"Farhan","Arman","Moin"}  # Set with mixed data types
# if you print this set, it will not maintain the order and will remove duplicates
# Sets are unordered collections of unique elements
print(s, type(s)) # Printing the set and its type
print(len(s)) # Length of the set       
print("Farhan" in s) # Checking if "Farhan" is in the set

s.add(786) # Adding an element to the set
print(s, type(s))      # Printing the set after adding an element
s.remove(1) # Removing an element from the set
print(s, type(s)) # Printing the set after removing an element
