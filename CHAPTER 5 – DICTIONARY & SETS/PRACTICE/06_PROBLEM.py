empty_dict = {}  # Initialize an empty dictionary
print("take two person name same") # this is to show that dictionary does not allow duplicate keys
w1 = input("Enter the first person's name: ") # Input first person's name
n1 = input(f"Enter the language of {w1}: ") # Input the language of the first person
empty_dict.update({w1: n1}) # Update the dictionary with the first person's name and language

w2 = input("Enter the second person's name: ")
n2 = input(f"Enter the language of {w2}: ")
empty_dict.update({w2: n2}) # Update the dictionary with the second person's name and language

w3 = input("Enter the third person's name: ")
n3 = input(f"Enter the language of {w3}: ")
empty_dict.update({w3: n3}) # Update the dictionary with the third person's name and language

w4 = input("Enter the fourth person's name: ")
n4 = input(f"Enter the language of {w4}: ")
empty_dict.update({w4: n4}) # Update the dictionary with the fourth person's name and language

print("THIS IS DICTIONARY OF YOUR INPUT PERSON AND THEIR LANGUAGE")
for key, value in empty_dict.items():
    print(f"{key} speaks {value}")
