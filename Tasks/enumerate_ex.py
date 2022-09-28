"""
Example for enumerate and list operations
enumerate()- It gives a tuple which starts  from 0, and it counts over iterables.
Returns a sequence of (index,items) tuples.

"""

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for idx, item in enumerate(list_1):
    del item

for idx, item in enumerate(list_2):
    list_2.remove(item)

for idx, item in enumerate(list_3[:]):
    list_3.remove(item)

for idx, item in enumerate(list_4):
    list_4.pop(idx)

print(list_1)
"""del item - it only deletes the item variable. so the list_1 data has not changed.
so the same list_1 data it returns
[1,2,3,4]
"""
print(list_2)
"""
remove- removes the first matching value but not index.
There is an iteration using the idx given to it. the value 1 with idx 0 is removed in first iteration,
list got updated and it remove idx 1 with value 3.  thereafter loop ends returns the list-
[2,4]
"""
print(list_3)
"""
The slicing has given to the list_3. there is no change in the list_3 during iteration. 
it removes all the items and returns the empty list 
[].
"""

print(list_4)
"""
pop - removes the value at a specific index and returns it. 
pop removes the value with provided index number. list_4 data will be updated after removing value 1 using idx 0
and remove  value 3 at idx 1.
"""
