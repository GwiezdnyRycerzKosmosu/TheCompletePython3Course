

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
