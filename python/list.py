#list are muttable ,ordered collection of differnt data types 


l=[1,2,3,4,5,3,4]
print(l[2:3])
co=l.count(4)
print(l[0])
print(co)
print(l[0]+l[1])

# if 8 in l:
#     print("yes")

# print(l[2:7])
# print(l[2:7:2])      #third index is a jump index 

lst = [i for i in range(10) if i%2==0]  # list comprehension 
print(lst)

# ls = [i*i for i in range(10)]
# print(ls)

# LIST METHODS 
l.sort()
print(l)
print(l[1])
l.sort(reverse=True)         #decending order
print(l)
l.reverse() 
print(l)
print(l.index(5))
print(l.count(4))
l.insert(5,6)  #(index , value)

# difference between extend and append 
print(l)
print("extend :")
l.extend([7,5,6])
print(l)
print("append:")
l.append([2,3,4])
print(l)
l.pop(4)
print(l)
k=[1,3,4]
c=k+l
print(c)

# copy 
# append 
# insert 
# extend
# concate  --> list1 + list2