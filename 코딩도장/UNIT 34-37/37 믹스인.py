class HelloMixIn:
    def greeting(self):
        print('hell0')

class Person():
    def __init__(self, name):
        self.name = name

class Student(HelloMixIn, Person):
    def study(self):
        print('studying')

class Teacher(HelloMixIn, Person):
    def teach(self):
        print('teaching')


sam = Student()
song = Teacher()

sam.greeting()
song.greeting()