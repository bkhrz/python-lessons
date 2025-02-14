list1 = [1, 1, 2]
list2 = [2, 3, 4]

list3 = []

for x in list1:
    if x not in list2:
        list3.append(x)

for x in list2:
    if x not in list1:
        list3.append(x)

print(list3)