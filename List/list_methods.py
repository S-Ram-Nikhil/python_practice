
# append method
# add elements to the end of the elements in the list
name = ['ram', 'nikhil']
name.append('Suryadevara')
print(name)
# extend method- increases the lenght of list. (add multiple elements)
marks = [60,70,80]
marks.extend([90,10])
print(marks)

# index() method - return the first appearance of the value
name = ['ram', 'nikhil', 'Suryadevara','nikhil']
s = name.index('nikhil')
print(s)

# min()-returns the lowest value.
names = ['ram',"nikhil",'surya']
marks = [80,90,70]
min_marks = min(marks)
min_index = marks.index(min_marks)
min_name = names[min_index]
print(min_name)

# clear()- removes all the elements
names.clear()
print(names)

# insert()- inserts the required value at the given position.
names = ['ram',"nikhil",'surya','nikhil']
names.insert(2,"venkat")
print(names)
# count()- return the number of elements.
print(names.count('nikhil'))
# pop()- removes the element at the given position
print(names.pop(2))
# nikhil

# remove()-removes the first occurance of the element.
names = ['ram',"nikhil",'surya','nikhil']
names.remove('nikhil')
print(names)
# ['ram', 'surya', 'nikhil']

# reverse()- reverse the order of the elements
names = ['ram', 'surya', 'nikhil']
names.reverse()
print(names)

# get all elements in a sublist of lists into a single list.
list_a = [[1, 2], [3, 4], [4, 5]]
final = []
for i in list_a:
    for each in i:
        final.append(each)
print(final)
# [1, 2, 3, 4, 4, 5]
