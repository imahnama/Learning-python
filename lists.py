# a list of comma-separated values between squuare brackets. Might conain different types, but usually the same typeself.
# lists are mutable - content can be changed
colors = ['Blue', 'Black', 'Brown', 'Grey']  #create a new list
print(colors)  #print list

#indexing - access items uisng indexes
last_three_colors = colors[-3:] #print last 3 items from the list
print(last_three_colors)

# Lists also suports operations  i.e concatenation
add_colors = colors + ['Orange', 'Purple']
print(add_colors)

#Types of methods
animals = ['Tiger', 'Horse', 'Kangaroo','Tiger']
animals.reverse()
print(animals)
# add item to the end of the list
animals.append('Fox')
print(animals)
# Remove the first item
animals.remove('Horse')
print(animals)
#insert an item at a given position
animals.insert(2,'Monkey')
print(animals)
# Remove item at a given position in the lists
animals.pop(2)
print(aimals)
# #######################################
numbers = [1,12,34,76,8,10,65,12,12]
# sort the lists
numbers.sort()
print(numbers)
# Return no of times x appears in the lists
num = numbers.count(12)
print(num)
# Return a shallow copy of the lists
numbers.copy()
print(numbers)

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
