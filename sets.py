#Sets may consist of various elements and is undefined
# They areimmutable

#defining a Set
numbers = {1, 2, 3}

#The order of elements printed is unimportant
key = set('qwerty')
print(key)

#Each element may enter the set only one
a = {1, 2, 3}
b = {2, 3, 1,2}
print(a == b)  #This prints true

#You can iterate over elements of a set using the for loop
even_num = {2, 4, 6, 8, 10}
for i in even_num:
    print(i)

#check length using the len funtion
even_num = {2, 4, 6, 8, 10}
print(len(even_num))

#check whether an element belongs to a set using the keyword in:
#similarly use the key word not in: to return a boolean type

fruits = {'orange', 'mango','banana'}
print('orange' in fruits, 'apples' not in fruits) #This returns True fro both

#use method add: to add elements in a Set
fruits.add('apples')
print(fruits)

#use method discard and remove to delete an element from a set. Difference is
#their behaviour incase deleted item is not in the set discard does nothing and delete throws an exception error
fruits.discard('apples')
print(fruits)
# fruits.remove('avocado')
# print(fruits)  #throws an exception key:error

#pop removes one random element from the set and if set is empty it throws a KeyError
fruits.pop()
print(fruits)

#Operations on Sets
a = {2, 4, 5}
b = {3, 7, 8}
c = a.union(b) # returns a union of the sets
print(c)

#use update to add all elements of array a to the set b
c = a.update(b)
print(c)

#Intersect
c = a.intersection(b)
print(c)

#Intersection_update (leaves in a only the items that belong to b)
c = a.intersection_update(b)
print(c)

#Difference
c = a.difference(b)
print(c)

#difference_update (removes all elements of b from a)
c = a.difference_update(b)
print(c)

#A <= B (writes in a the symmetric diff of sets a and b)
c = a.symmetric_difference_update(b)
print(c)

#issubset returns true if a is a subset of b
c = a.issubset(b)
print(c)
#A >= B issuperset returns true if b is a subset of a
c = a.issuperset(b)
print(c)
