# Dictionary Comprehension
triple_dict = dict()
for num in range(2, 15):
    triple_dict[num] = num*num
print(triple_dict)

# dictionary comprehension-
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

# using conditions -
dict1 = {'ram': 18, 'nikhil': 48,}

final_dict = {k: v for (k, v) in dict1.items() if v % 2 == 0}
print(final_dict)

#  Multiple if -
dict1 = {'ram': 19, 'nikhil': 38,}

final_dict = {k: v for (k, v) in dict1.items() if v % 2 != 0 if v < 40}
print(final_dict)

# if else-
dict2 = {'ram': 19, 'nikhil': 46,}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in dict2.items()}
print(new_dict_1)
