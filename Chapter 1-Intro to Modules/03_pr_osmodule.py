import os
print(os.listdir())   
#os module works with the operating system. Here, os.listdir() function returns everything that is present inside the directory.

print(os.getcwd())  #gives current working directory

# os.chdir('path')  => this will change current working directory
os.chdir('C:\\Users\\admin\OneDrive - Nepal College of Information Technology\\Desktop\\Notes of Python')
print(os.getcwd())
print(os.listdir())