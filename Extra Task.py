Extra Task
#1)
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

# 2)
# is python 2.0 version
# import sys
# range_a = range(1,1000)
# xrange_a= xrange(1,1000)
# print(range_a)
# print(xrange_a)
# print(type(range_a)
# print(type(xrange_a))

# 3)
list_it = range(1, 1100)
list_ans = [i for i in list_it if (i % 3 == 0) & (i % 2 == 0)]
print(list_ans)

# 4)
string_val = input("Enter a string:")
string_rev = string_val[::-1]
for letter in string_rev:
    if
letter in 'aeiou':
print(letter)
print("index is", string_rev.index(letter))

# 5)
string_it = "hello my name is abcde"
list_words = [i for i in string_it.split()]
print(list_words)
list_evenlen = [i for i in list_words if len(i) % 2 == 0]
print(list_evenlen)

# 6)


class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i


print("index1=%d, index2=%d" % py_solution().twoSum((1, 2, 3, 4, 5, 6, 7, 8, 9, -1), 8))


# 7
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

# 8
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

# 9
given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result_list = []
for i in given_tuple:
    if i % 2 == 0:
        result_list.append(i)

result_tuple = tuple(result_list)
print(result_tuple)
