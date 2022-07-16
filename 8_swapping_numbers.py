# Here, we are trying to swap the values of two variables. Suppose, a=5 and b=7, then we are trying to have a=7 and b=5.

a=5
b=7

print("A:",a)
print("B:",b)

temp=a   #value of a is copied in some other variable temp
a=b   #now we can overwrite value of a by b.
b=temp #then value previously stored in temp i.e previous value of a overrides present value of b
print("A:",a)
print("B:",b)

#In the above example, we used thied variable temp to swap two values. Let us try swapping values without using third variable now.

p=6
q=7
p=p+q   #6+7=13
q=p-q   #13-7=6
p=p-q   #13-6=7
print(p)   #7
print(q)   #6

''' Using above formula, we can swap the value of two variables without using the third variable. But theres is something wrog with it. 

6 uses 3 bits i.e 110 and 7 also uses 3 bits 111 but 13 requires 4 bits so we are wasting 1 extra bit. Thats why we use XOR(^) method for it.'''

m=8
n=4
m=m^n
n=m^n
m=m^n
print(m)
print(n)


j=3
k=1
j,k=k,j #this kind of swapping only works if used in single line, else for multiple lines, it wont work.
print(j)
print(k)

# How is it able to swap in above line?
# Because solving always starts from right and at first k,j i.e 1,3 will be stored in stack and with the method of rotation, it will be assigned to j and k in the background.
