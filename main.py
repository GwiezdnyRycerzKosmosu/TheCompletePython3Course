

def print_something(name, age):
    print("My name is " + name + " and my age is "+ str(age))
print_something("Mateusz", 31)

def print_something2(name, age):
    print("My name is", name, "and my age is", age)
print_something2("Mateusz", 31)

#def of a function with default values
def print_something3(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)
print_something3("Mateusz")

#def of a function with default values, giving keyword argument
# Note:"none is similar to null in other languages and is a boolean"
def print_something4(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)
print_something4(age = 100)
print_something4(age = 100, name="Stefan")

#loop and infinitive arguments
def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("NIck", "King", "Shannon", "Geralt", "Henry")

#def function which return sth
def do_math(num1, num2):
    return num1+num2
math1=do_math(8,43)
math2=do_math(88,43)
print("First sum is ",math1," and the second sum is ",math2)

#if, elif, else statement
check = "Hamburger"
if check == False:
    print("It is false")
elif check == "Hamburger":
    print("Yummmm, hamburgers!")
else:
    print("It is actually equal to true")

# while/for loops
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

run=True
current=0

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 5


#24.Importing libraries into a script REGEXP
import re
string ="'I am not YELLING', she said. Though we knew it not to be true"
print(string)
new=re.sub('[,.+" "]','',string)
print(new)

new2=re.sub('[A-Z]','',string)
print(new2)

string2= string + "6 2222 + 888"
print(string2)
new3= re.sub('[^0-9]','',string2)
print(new3)