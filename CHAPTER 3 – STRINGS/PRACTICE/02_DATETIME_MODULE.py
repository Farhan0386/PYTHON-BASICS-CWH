import datetime

name = input("ENTER YOUR NAME: ")
time =str(datetime.datetime.now())

letter = '''HELLO, <|NAME|>
YOU ARE SELECTED
<|DATE|>'''
print(letter.replace("<|NAME|>", name).replace("<|DATE|>", time))