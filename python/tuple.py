# TUPLES are immutable :

t=((2,3,4),(5,6,7))
print(t[0][2])

tup1=(1,2,7.8,-67.9,"smit")
tup2=(10,6)
print(len(tup1))
print(sorted(tup2))
print(tup1[3])



#'tuple' object does not support item assignment
#t[1][0]=0

#print(min(tup2))
#print(max(tup2))


# print(type(tup1))
# print(type(tup2))
# print(type(tup3))


# indexing :
# print(tup1)
# print(tup1[0])
# print(tup1[-1])

#slicing :
print(tup1[1:])
print(tup1[-1:])
print(tup1[::2])

print(len(tup1))

# nested tuple :

tup3=(tup1,tup2)      # tup3=( (tup1),(tup2) )

# print(tup3)
# print(tup3[0][4])
#print(len(tup3[0]))               # it returns 5 
tup3 = tup1 + tup2
print((tup3))
# print(tup3)

print(tup1.count("jaymin"))
print(tup1.index("smit"))

# tuple into list :
p=list(tup1)
print(p)

# list into tuple :
list=[1,2,3,4,5,6,7]
t=tuple(list)
print(t)

tuple4=(10,)*4
print(tuple4)                    #(10,10,10,10)
