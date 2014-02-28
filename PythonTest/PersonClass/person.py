# coding=utf-8

def say(word):  
    print(word) 


class Person:

    ''''' 
    classdocs 
    '''
    Count = 0

    def __init__(self, name, age):
        ''''' 
        Constructor 
        @param: name the name of this person 
        @param: age the age of this person   
        '''
        self.name = name
        self.age = age
        Person.Count += 1

    def detail(self):
        ''''' 
         the detail infomation of this person 
        '''
        print('name is ', self.name)
        print('age is ', self.age)
        print('there are ' + str(Person.Count) + " person in the class")
