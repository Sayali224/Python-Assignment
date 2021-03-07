# Python-Assignment

1)
def main():
    try:
        name = 'sayali
    except SyntaxError as error:
        Logging.log_exception(error)
    except Exception as exception:
        Logging.log_exception(exception, False)


if __name__ == "__main__":
    main()

#2)
while True:
    try:
        name = input("Enter the file name: ")
        s=open(name, 'r')
        print(s.read())
        break
    except:
        print('File name is not correct')

#3)
while True:
    s=input("Enter a number  ")
    if len(s) == 4:
        print(s)
        break
    else:
        print("The number entered is too short/long")

#4)
print('Enter correct username and password to continue')
count=0
password="321"
username="Sayali"

while password!='321' and username!='Sayali' and count<4:
    username=input('Enter username: ')
    password=input('Enter password: ')

    if password=='321' and username=='Sayali':
     print('Access granted')

    else:
        print('Access denied. Try again.')
        count-=1

#6)
x=open("demo.txt", "r", encoding="abc123")
a=x.read()
words=a.split()
for i in words:
    if len(i) % 2 == 0:
        print(i)
