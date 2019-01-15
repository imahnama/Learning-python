# a list of comma-separated values between squuare brackets. Might conain different types, but usually the same typeself.
# lists are mutable - content can be changed
colors = ['Blue', 'Black', 'Brown', 'Grey']  #create a new list
print(colors)  #print list

#indexing - access items uisng indexes
newcolors = colors[-3:] #print last 3 items from the list
print(newcolors)

# Lists also suports operations  i.e concatenation
newcolors1 = colors + ['Orange', 'Purple']
print(newcolors1)

#Types of methods
Animals = ['Tiger', 'Horse', 'Kangaroo','Tiger']
Animals.reverse()
print(Animals)
# add item to the end of the list
Animals.append('Fox')
print(Animals)
# Remove the first item
Animals.remove('Horse')
print(Animals)
#insert an item at a given position
Animals.insert(2,'Monkey')
print(Animals)
# Remove item at a given position in the lists
Animals.pop(2)
print(Animals)
# #######################################
Numbers = [1,12,34,76,8,10,65,12,12]
# sort the lists
Numbers.sort()
print(Numbers)
# Return no of times x appears in the lists
Num = Numbers.count(12)
print(Num)
# Return a shallow copy of the lists
Numbers.copy()
print(Numbers)

# using list as stacks(last-in, first-out)
stack = ['cate', 'Eva', 'Asha']
stack.append('Sue')
print(stack)
# last element removed
stack.pop()
print(stack)

# using lists as queues(first-in,first-out)
# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
from collections import deque
queue =deque(['Nama', 'Ima', 'Tima'])
queue.append('Kasow')
print(queue)
queue.popleft()  #first item is removed
print(queue)

# List comprehensions (provides a concise way to create lists)
squares = [x ** 2 for x in range(10)]
print(squares)
