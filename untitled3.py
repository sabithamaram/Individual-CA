# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hRQaEkZj26JaG-z7-_9nzrw-rJ0sBvMI
"""

import heapq

students = []
heapq.heapify(students)

def add(self, data): 
    heapq.heappush(students,data)

def retrieve(self): 
    if len(students) == 0:
        print("No students left to retrieve")
    else :
        print(students[0])
        heapq.heappop(students)

if __name__ == '__main__': 
    add(students,{'2': { "Name" : "Himaja" , "Course Code" : "CS1"}})
    add(students,{'1': { "Name" : "Sabitha" , "Course Code" : "CS2"}})
    add(students,{'3': { "Name" : "Harsha" , "Course Code" : "CS3"}})
    print(list(students))
    retrieve(students)
    print(list(students))
    retrieve(students)
    print(list(students))
    retrieve(students)
    print(list(students))
    retrieve(students)