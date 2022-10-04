names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']

print(names.count("John"))
d= {}
for i in range(len(names)):
    dict_1 = names[i]
    count = 0
    for j in range(i,len(names)):
        if names[j] == names[i]:
            count += 1
    count = dict({dict_1: count})
    if dict_1 not in d.keys():
        d.update(count)
print(d)