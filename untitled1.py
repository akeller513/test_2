# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:11:11 2022

@author: kealz
"""

def hello_func(greeting, name="you"):
    return '{}, {}'.format(greeting,name)

print(hello_func("hi")) 

def student_info(*args, **kwargs): #don't know how many positional and keyword arguments there will be
    """Docstrings describe function and arguments """ 
    print(args) #tuple
    print(kwargs) #dictionary
    
student_info("math", "art", name="john", age=22)

courses = ['math', 'art']
info = {'name': 'john', 'age': 22}

student_info(*courses, **info) #use * to pass arguments and unpack them 

x = 'global x'

def test(z):
    global x #grab global varible to use with 
    x = 'local x'
    print(x)
    
print(x)
test('local z')

print(hello)

