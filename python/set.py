# set are unordered they are not define on order
# set item does not support indexing  
# generally sets are muttable 

s1=frozenset((1,2,3,4,4))   # we create immutable set s1 when we converting into frozenset 
print(s1)            

set1 ={1,3,5,"smit",78.9,'smit',5,True}
set2={}
set3=set()                  #another method to define set
print(type(set1))
print(type(set2))
print(type(set3))

#set item does not support item assignment 
# set1.add(89)
# print(set1)
# set1.remove(89)
# print(set1)
n=set1.pop()   #random value pop 
# print(set1)
set1.discard(1)       #if 1 not exist code run  fluently 
# set1.clear()
print(set1)
print(n)
set1.add((2,3,4))
print(set1)
# set1.add([4,5,6])      gives an error
# print(set1)
s1={1,2,3,4,5}
s2={2,3,4,5,6,7}
print(s2.difference(s1))


'''
add 
remove
pop
clear
discard
'''