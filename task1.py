#List
#Create a List
my_list = [25,85,45,16]
print("Initial List",my_list)
#Add an element to the List
my_list.append(34)
#Remove an element from the List
my_list.remove(45)
#Modify an element in the List
my_list[2]= 56
print("Updated List",my_list)

#Dictionary
#Create a Dictionary
my_dict = {'a': 65,'b': 24,'c': 49,'d': 18}
print("Initial Dictionary",my_dict)
#Add a key-value pair from the Dictionary
my_dict['e']=71
#Remove a key-value pair from the Dictionary
del my_dict['c']
#Modify a value in the Dictionary
my_dict['a'] = 38
print("Updated Dictionary",my_dict)

#Set
#Create a Set
my_set = {79,43,15,28,13}
print("Initial Set",my_set)
#Add an element to the Set
my_set.add(88)
#Remove an element from the Set
my_set.remove(28)
print("Updated Set",my_set)