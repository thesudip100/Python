# WAP to fill in a letter template given below with name and date.

letter= '''Dear <|name|>,\n\tyou are selected!\n\t<|Date|>'''
print(letter)
name = input("Enter the name:")
letter=letter.replace("<|name|>", name)
date = input("Enter the date of joining:")
letter=letter.replace("<|Date|>", date)
print(letter)

