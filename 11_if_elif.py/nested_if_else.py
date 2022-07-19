# If there are if statements inside the if statement in python, then they are called as nested if else. Let us see a code below to understand this.

x=8
if(x%2==0):
    print("even number")
    if(x>5):    #if statement inside if statement
        print("The number is greater than 5")
    else:
        print("The number is less than 5")
else:
    print("Odd")

#In the above program, there is an if statement inside the if statement. When if(x%2==0) will be true, the code inside it will be executed. So, even number will be printed. Then again, it will check if the x is grater than 5 or not: if it is greater then if statement will run else "else" statement will run. If (x%2==0) was false, then Print("Odd") statement will run.



#WAP to print one, two, three, four when user enters 1,2,3,4.

x=int(input("Enter a number from 1 to 4:"))
if(x==1):
    print("One")
elif(x==2):
    print("two")
elif(x==3):
    print("three")
elif(x==4):
    print("four")
else:
    print("wrong entry")

# In if statement, every lines of code will be parsed but in elif statement, not every lines will be parsed. When it finds right one, the code will stop. Here, if we enter 2, it will check till second elif statement only and once it finds x==2, then it will stop the execution. But the case wont have been same when we had used all if statement instead of elif statement. If "if"  statement were used, then even after it finds right answer at x==2, it will still check for x==3 and x==4 which will increase time of code and decrease the speed of the task.


