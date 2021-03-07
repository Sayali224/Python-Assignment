# Python-Assignment

1)
x = input ("Enter a value:")
x = int(x)
if (x%3 == 0) and (x%5 == 0):
   print("Consultadd Python Training:")
if (x%3 == 0):
    print("Consultadd")
if (x%5 ==0):
    print("C")
    if result <0 :
        print("Negative")

# 2)
y = input("Select a value:")
y = int(y)
if y == 1:
   x1,x2 = input("Enter the two values:").split()
   result= int(x1)+int(x2)
   print("Addition:", result)
   if result <0 :
        print("Negative")

if y == 2:
   x1,x2 = input("Enter the two values:" ).split()
   result= int(x1)-int(x2)
   print("Subtraction:",result)
   if result <0 :
        print("Negative")

if y == 3:
   x1,x2 = input("Enter the two values:" ).split()
   result= int(x1)*int(x2)
   print("Multiplication:",result)
   if result <0 :
        print("Negative")

if y == 4:
   x1,x2 = input("Enter the two values:" ).split()
   result= int(x1)/int(x2)
   print("Division:",result)
   if result <0 :
        print("Negative")

if  y == 5:
    x1,x2,x3 = input("Enter three values:").split()
    result= (int(x1)+int(x2)+int(x3))/3
    print("Average:",result)
    if result <0 :
        print("Negative")


#3)
a = 10
b = 20
c = 30
avg = (a+b+c) / 3
print("avg:",avg)
if ( avg > a) and (avg > b) and (avg > c):
    print("Avg is higher than a,b,c:")
elif(avg > a) and (avg > b):
    print("avg is higher than a,b,c:")
elif(avg > a) and (avg > c):
    print("avg is higher than a,c:")
elif(avg > b) and (avg > c):
    print("avg is higher than b,c:")
elif(avg > a):
    print("avg is just higher than a:")
elif(avg > b):
    print("avg is just higher than b:")
elif(avg > c):
    print("avg is just higher than c:")


#5)
n1=[]
for x in range (2000,3200):
    if (x%7==0) and (x%5!=0):
        n1.append(str(x))
print(','.join(n1))

#6)
x=123
for i in x:
    print(i)

i = 0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print("error")

count = 0
while True:
    print(count)
    count+=1
    if count>=5:
        break

#7)
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")

#8)
s = input("Input a string")
d=l=0
for a in s:
    if a.isdigit():
        d=d+1
    elif a.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

