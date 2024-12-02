#author : smit satani         this is single line comment 
# frist program
# in python all tokens are considered as an object 
print("hello world")
print("bye")


# multiple comment  
'''         
print("hello world")
'''
# other multiline comment 
"""
print("hello world")
"""  


print("hii",6,7)  # by default end="\n"  
        
print("hii",6,7,sep=" ", end="\n")
print("smit satani")
print("ohk")

a=input("enter string:")
vowel="aeiouAEIOU"
count=0
for i in a:
        if i in vowel:
         count=count+1
print(f"{count} vowels In this string ")   # fstring 

