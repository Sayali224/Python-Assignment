# Python-Assignment

1)
# method1
a = 1
b = 20.34
c = "hello"
d = 4 + 5j
e = True
f = 56
g = 65
h = 78
i = 44
j = 98
data = [(a, b, c, d, e, f, g, h, i, j)]
print(data)

# method2
data1 = [None] * 10
data1[0] = 1
data1[1] = 20.34
data1[2] = "Hello"
data1[3] = 6 + 7j
data1[4] = False
data1[5] = 5
data1[6] = 6
data1[7] = 7
data1[8] = 8
data1[9] = 9
print(data1)

# 2)
l = [1, 2, 3, 4, 5]
print(l)
print(l[2:4])
print(l[:3])

# 3)
# sum of list
l1 = [10, 20, 30, 40]
sum_list = sum(l1)
print(sum_list)

# multiply list
import numpy as np

mul_list = np.prod(l1)
print(mul_list)

# 4)
l2 = [23, 16, 54, 70, 92]
min_list = min(l2)
print(min_list)
max_list = max(l2)
print(max_list)

# 5)
l3 = [12, 5, 34, 6, 75, 9, 66, 73]
l4 = [i for i in l3 if i % 2 != 0]
print(l4)

# 6)
l5 = []
for i in range(1, 31):
    l5.append(i * i)
print(l5[:5])
print(l5[-5:])

# 7)
l6 = [1, 3, 5, 7, 9, 10]
l7 = [2, 4, 6, 8]
l6[-1:] = l7
print(l6)

# 8)
dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {}
for d in (dict_a, dict_b):
    dict_c.update(d)
print(dict_c)

# 9)
val = int(input("Enter a number:"))
dict_d = {}
for i in range(1, val + 1):
    dict_d[i] = i * i
print(dict_d)

# 10)
values = input("Enter values sepreated with commas:")
list_val = values.split(",")
tuple_val = tuple(list_val)
print(list_val)
print(tuple_val)

# 13)
list_x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]

# access list [1,2,3,4]
print(list_x[5][:4])

# Access list [600,  700]
print(list_x[6:8])

# Access list [100, 300, 500, 600, 800]
print(list_x[0::2])

# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(list_x[::-1])

# Access list [10]
print(list_x[5][5][0])

# Access list [ ]
print(list_x)

# 14)
# is python 2.0 version
# import sys
# range_a = range(1,1000)
# xrange_a= xrange(1,1000)
# print(range_a)
# print(xrange_a)
# print(type(range_a)
# print(type(xrange_a))

# 16)
list_it = range(1, 1100)
list_ans = [i for i in list_it if (i % 3 == 0) & (i % 2 == 0)]
print(list_ans)

# 17)
string_val = input("Enter a string:")
string_rev = string_val[::-1]
for letter in string_rev:
    if
letter in 'aeiou':
print(letter)
print("index is", string_rev.index(letter))

# 18)
string_it = "hello my name is abcde"
list_words = [i for i in string_it.split()]
print(list_words)
list_evenlen = [i for i in list_words if len(i) % 2 == 0]
print(list_evenlen)

# 19)


class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i


print("index1=%d, index2=%d" % py_solution().twoSum((1, 2, 3, 4, 5, 6, 7, 8, 9, -1), 8))


# 20)
def splitevenodd(A):
    evenlist = []
    oddlist = []
    for i in A:
        if (i % 2 == 0):
            if len(evenlist) < 5:
                evenlist.append(i)
            else:
                print("Even List has reached full capacity,cannot add", i)
                break
        else:
            if len(oddlist) < 5:
                oddlist.append(i)
            else:
                print("Odd List has reached full capacity,cannot add", i)
                break
    print("Even lists:", evenlist)
    print("Odd lists:", oddlist)


# Driver Code
A = list()
n = int(input("Enter the size of the First List ::"))
print("Enter the Element of list between 1-50 ::")
for i in range(int(n)):
    k = int(input(""))
    A.append(k)
splitevenodd(A)

# 21)
string_ex = "12abcbacbaba344ab"
# remove numbers
string_result = ''.join([i for i in string_ex if not i.isdigit()])

print(string_result)
all_freq = {}

for i in string_result:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(str(all_freq))

# 22)
given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result_list = []
for i in given_tuple:
    if i % 2 == 0:
        result_list.append(i)

result_tuple = tuple(result_list)
print(result_tuple)
