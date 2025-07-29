import pyjokes
# FIRST WE IMPORT THE EXTERNAL MODULE
# THEN WE USE IT
# pyjokes is an external module that provides jokes
# You can install it using pip: pip install pyjokes
jokes=pyjokes.get_joke() #FIRST WE CREATE A VARIABLE IN WHICH WE STORE THE FUNCTION OF MOUDULE      
# pyjokes.get_joke() returns a random joke
# Now we can print the joke 
print(jokes)
print("This is an external module example.")   