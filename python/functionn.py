# def calculate(a,b):             #function definition
#     print(a+b)

# a=int(input("enter a :"))
# b=int(input("enter b :"))

# print("sum of a and b is : ")
# calculate(a,b)

#functions arguments:
# Default Arguments
# Keyword Arguments     -->    passing in the form of key value 
# Variable length Arguments

def name(*name):         # ----> accept the arguments in the form of (tuple)
    print("Hello,", name[0], name[1], name[2],name[4])

name("James", "Buchanan", "Barnes",7,8,9,)

# Required Arguments    ----> accept the arguments in the form of (dictionary)
def name(**name):
    print("Hello,", name['fname'], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")


