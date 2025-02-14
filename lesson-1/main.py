#a = input("Your age:")
#print(a)
from itertools import count

# n = 73.4842248763
# print(f"{n:.5f}")

# a = "Hello World"
# print(a[-2:0])

# word = input("Enter a word: ")
# #last_character = word[-1]
# print(f"Last character is {word[-1]}")

# a = "hello"
# b = "world"
# c = a==b
# print

# (c)
#
# a=[1,2,3]
# b = a.copy()
# a.append(2)
# print(a)
# print(b)
#
# mylist = input('enter the list: ').split()
# num = int(input('How many times does it need to be repeated: '))
#
# newlist1 = []
#
# for x in mylist:
#     newlist1.extend(num*[x])
#
# print(newlist1)
#
# #
# # a = [ 'a' , 'b', 'qe', 'h', 'r']
# # a.sort()
# # print(a)
#
# a = "jvhdfr"
# print(a.count('j'))

# s1 = {"a", "b", 'c'}
# s2 = {"b"}
# if s2 in s1:
#     print('s2 is subset of s1')
#
# s1 = {"a", "b", 'c'}
# print(s1.pop())

for i in range(2,100,1):
    a = True
    for j in range(2,i//2+1,1):
        if i % j == 0:
            a = False
            break
    if a:
        print(i)