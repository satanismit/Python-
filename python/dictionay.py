# dictionary == key value pair  
# ordered collection of items
# it can be changable and indexed..(mutable)
dic ={"masala":"spicy","Ginger":"Zesty","green":"mild"}

# accessing element 
print(dic["masala"])   # gives an error if key dose not match
print(dic.get("Ginger"))  # return none if key dose not match 

# updating an element 
dic["green"]="fresh"
print(dic)
dic.update({'masala':'hot'})
print(dic)

# remove an element 
dic.pop("Ginger")
dic.popitem()
print(dic)
del dic["masala"]
print(dic)

# print(dic.values())
# print(dic.keys())
print(dic.items())

# nested dictionary 
car1={'model':'Harrier','model':'tata'}
car2={'name':'safari'}

car={'kcar':car1,'kname':car2}
print(car['kcar'])

print(car['kcar']['model'])