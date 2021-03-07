# Python-Assignment

def multiple_element(n):
    return n*n
x=[1,2,3,4,5,6]
y=list(map(multiple_element, x))
print(y)

string_ex = "Hello World"
res= [i for i in string_ex if i.isupper()]
print("The uppercase letters are : ",str(res))

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
res_dict = dict(zip(Student,capital))
print ("Resultant dictionary is : " +  str(res_dict))

rev_string = "Consultadd Training"
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

for char in rev_str(rev_string):
    print(char)
