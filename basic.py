# dict1={}
# no_of_terms=int(input("Enter the numbers of terms "))
# for i in range(no_of_terms):
#     key=input("Enter a key")
#     value=input("Enter a value ")
#     dict1[key]=value
# print(dict1)

# dict2=dict({'abc':12,'nepal':143432})
# print(dict2)
# new_dict=dict([('steve',2323),('frank',2323)])
# print(new_dict)

new_dict1= {x: x**2 for x in (2,4,6)}
print(new_dict1)

# for key,value in new_dict1.items():
#     print(key,value)

# for index,key in enumerate(new_dict1):
#     print(index,key)

# for key in new_dict1.keys():
#     print(key)

# for value in new_dict1.values():
#     print(value)

value=new_dict1.get(3,'key not found')
print(value)
# dicitionary.pop(key,defaults)
value =new_dict1.pop(2,'Entery not found')
print(value)
print(new_dict1)
key,value=new_dict1.popitem()
print(new_dict1)

new_dict1.clear()
print(new_dict1)