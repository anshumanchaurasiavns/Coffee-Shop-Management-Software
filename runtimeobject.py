from tkinter import *

class Person(object):
    def __init__(self, name):
        self.name = name
   

people = {}
while True:
    a_name=""
    a_name = input("Enter a name:")

    if a_name == 'done':
        break

    people[a_name] = Person(a_name)

    print("I made a new Person object. The person's name is %s." % a_name)
print(people)
#print(repr(people))