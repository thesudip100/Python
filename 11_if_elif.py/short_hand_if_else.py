# We can also use if-else statement in shortcut form and for this, we can use following syntax;

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))

#to check which one is greater
print(f"{b} is greater than {a}") if a<b else print(f"{a} is greater than {b}")