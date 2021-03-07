# Python-Assignment

1)

def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1


print(string_reverse('1234abcd'))


# 2)
def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass


print("Original String : ", s)
print("No. of Upper case characters : ", d["UPPER_CASE"])
print("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('Story Of My Life')


# 3)
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))

# 4)
items = [n for n in input().split('-')]
items.sort()
print('-'.join(items))

# 5)
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)

    # 6)


def calculateSum(a, b):
    s = int(a) + int(b)
    return s

    # 7)


def printVal(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)


s1, s2 = input().split()
printVal(s1, s2)


# 8)
def printTuple():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print
    tuple(li)


printTuple()


# 9)
def showNumbers(limit):


limit = int(input("Give me a number. "))

for i in range(0, limit + 1):

    if i % 2 == 0:

        print(str(i) + ":" + 'EVEN')


    else:

        print(str(i) + ":" + 'ODD')

# 10)
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = filter(lambda x: x % 2 == 0, li)
print
evenNumbers

# 11)
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, li))
print
evenNumbers


# 12)
def throws():
    return 5 / 0


try:
    throws()
except ZeroDivisionError:
    print
    "division by zero!"
except Exception, err:
    print
    'Caught an exception'
finally:
    print
    'In finally block for cleanup'

    # 13)
lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
joinedlist = []
for list in lists:
    joinedlist += list

print(joinedlist)

# 14)
What is the
output
of
the
following
codes:
(i)


def foo():
    try:
        return 1
    finally:
        return 2


k = foo()
print(k)

(ii)


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')


a()

O / P: If
the
try statement reaches a break,
continue or return statement, the finally clause
will
execute
just
before
the
break, continue or return statement’s
executes.
If
a finally clause
includes
a
return statement, the
returned
value
will
be
the
one
from the finally clause’s
return statement, not the
value
from the

try clause’s return statement.
