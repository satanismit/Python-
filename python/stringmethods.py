# #Strings are immutable(they do not change)
a="    smit  !!!! !!!! smit "

# print(len(a))          
# print(a.upper())
# print(a.lower())
print(a.strip())                # remove strip 
print(a.replace("smit","satani").strip())
print(a.split("!"))
# print(a.center(22))
str = "i Am aa boY"
# print(str.capitalize())              # I am a boy
# print(a.count("!"))
# print(a.endswith("t"))

# print(a.endswith("!",2,12))    # check in index 2 to 12

# print(str.find("a",6))   # if string does not exists it return -1
# print(str.index("aa"))     # if string does not exists it gives error
print(str.isalnum())
b= "smitsatani"
print(b.isalpha())
# print(b.islower())
# str1 ='wish you a very "happy birthday" \n '
# print(str1)
print(str.isprintable())   

# print(str[4].isspace())

c="World Health organization"
# print(c.istitle())      # reutrn true if all first letter of word is capital 

# print(c.swapcase())     #  wORLD hEALTH oRGANIIZATION
print(c.title())

