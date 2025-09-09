import datetime

name = input("ENTER YOUR NAME: ")
time =str(datetime.datetime.now())

letter = '''HELLO, <|NAME|>
YOU ARE SELECTED
<|DATE|>'''
print()
print("HERE BY THE HELP OF DATE TIME MODULE WE ARE ADDING DATE AND TIME IN THE LETTER")
print(letter.replace("<|NAME|>", name).replace("<|DATE|>", time))