
marks = {
    "Farhan": 100,
    "Rahil": 56,
    "Moin": 23,
    "Arman": 99,
}
print(marks.items())   # Returns a view object that displays a list of a dictionary's key-value tuple pairs
print(marks.keys())    # Returns a view object that displays a list of all the keys in the dictionary
print(marks.values())  # Returns a view object that displays a list of all the values in the dictionary
marks.update({"Farhan": 99, "Arman": 100}) # Update the value of existing keys
print(marks) # printing the updated dictionary
print(marks.get("Farhan")) # Accessing value using key
print(marks.get("Farhan2")) # Prints None
print(marks("Farhan2")) # it will throw an error
