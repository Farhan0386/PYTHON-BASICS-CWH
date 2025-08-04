variable1="HELLO THIS PROGRAM IS ABOUT TO   FIND FUNCTIO IN STRING  I GIVE DOUBLE SPACE IN THIS STRING AND BY THE HELP OF FUNCTION WE CAN FIND THEIR INDEX IN THE STRING"
# This code finds the index of the first occurrence of double spaces in the string
# in python index counting starts from 0
find_function=variable1.find("  ")
print(find_function) # this will print the index of the first double space

print("THIS PROGRAM IS IMPORTED FROM  ANOTHER NOW WE ARE GOING TO REPLACE DOUBLE SPACE WITH SINGLE SPACE IN THE STRING")
replace_function=variable1.replace("  ", " ") # this will replace double spaces with single space
print(replace_function) # this will print the string with single spaces

find_function2=replace_function.find(" ") # this will find the index of the first single space in the modified string
print(find_function2) # this will print the index of the first single space