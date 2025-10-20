print('''this is a dictionary practice problem in which 
       You have to create a dictionary with 4 words and their english form.''')
dict1={}  # Initialize an empty dictionary
w1=input("Enter the first word: ")  # Input first word 
m1=input("Enter the english form of first word: ")  
dict1.update({w1:m1})  # Update the dictionary with the first word and its English form
w2=input("Enter the second word: ")  # Input second word
m2=input("Enter the english form of second word: ") 
dict1.update({w2:m2})  # Update the dictionary with the second word and its English form   
w3=input("Enter the third word: ")  # Input third word
m3=input("Enter the english form of third word: ")
dict1.update({w3:m3})  # Update the dictionary with the third word and its English form
w4=input("Enter the fourth word: ")  # Input fourth word
m4=input("Enter the english form of fourth word: ")
dict1.update({w4:m4})  # Update the dictionary with the fourth word and its English form

print(dict1)  # Print the dictionary to show the current state 
# this will display all key-value pairs in the dictionary in the format {key: value}
# If you want to print each key-value pain in a specific format, you can do so like this:
for key,value in dict1.items():
    print(f"{key}-{value}")  # Change '-' to any separator you like
# This will print each key-value pair in the format "key-value"