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
    try :
        response = int(raw_input("Choose an option\n1 - Add student\n2 - Retrieve student\n3 - Show all students\n4 - Exit\n"))
    except :
        print(" Please input number only")
        response = 5
    while response > 4 or response < 1:
        print("Enter valid option\n")
        try :
            response = int(raw_input())
        except :
            print(" Please input number only")
            response = 5
    while response != 4:
        if response == 1:
            Name = str(raw_input("Enter the student name : "))
            try :
                Number = int(raw_input("Enter student number : "))
            except :
                print("Not a number")
                Number = 0
            while Number > 99999999 or Number < 10000000 : 
                Number = int(raw_input("Enter a valid student number : "))
            Course = str(raw_input("Enter Course Code : "))
            add(students,{ Number : { "Name" : Name, "Course Code" : Course}})
        elif response == 2:
            retrieve(students)
        elif response == 3:
            print(list(students))
        try :
            response = int(raw_input("Choose an option\n1 - Add student\n2 - Retrieve student\n3 - Show all students\n4 - Exit\n"))
        except :
            print(" Please input number only")
            response = 5
        while response > 4 or response < 0:
            print("Enter valid option\n")
            try :
                response = int(raw_input())
            except :
                print(" Please input number only")
                response = 5
    # add(students,{'2': { "Name" : "Himaja" , "Course Code" : "CS1"}})
    # add(students,{'1': { "Name" : "Sabitha" , "Course Code" : "CS2"}})
    # add(students,{'3': { "Name" : "Harsha" , "Course Code" : "CS3"}})
    # print(list(students))
    # retrieve(students)
    # print(list(students))
    # retrieve(students)
    # print(list(students))
    # retrieve(students)
    # print(list(students))
    # retrieve(students)
