"""Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates"""

diction_movie= {
"interstaller":9,
"iron-man":8,
"thor":9.8,
"endgame":10,
"radhe":2,
"dabbange":1}
print(diction_movie)

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:


print(diction_movie["radhe"])#To determine how many items a dictionary has, use the len() function:

print(len(diction_movie))

#From Python's perspective, dictionaries are defined as objects with the data type 'dict':

print(type(diction_movie))

# Accessing items
#There is also a method called get() that will give you the same result:

#The keys() method will return a list of all the keys in the dictionary.

"""     Change values  """
#You can change the value of  specific item by referring to its key name:``

diction_movie= {
"interstaller":9,
"iron-man":8,
"thor":9.8,
"endgame":10,
"radhe":2,
"dabbange":1}
print(diction_movie)
"""
                Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
"""
# we add new movie 
diction_movie["spiderman"]=9.7
print(diction_movie);  # spider man is added to dictionary

#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
diction_movie.update({"logan":9.9})   # use curly braces
print(diction_movie) 

#Loop Through a Dictionary
 #You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

for x in diction_movie:
    print(x);