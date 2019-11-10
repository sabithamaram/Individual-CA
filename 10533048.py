class Node:
    def __init__(self, val, priority,Name,Course):
        self.val = val
        self.next = None
        self.priority = priority
        self.Name = Name
        self.Course = Course

class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front == None
    def push(self, val, priority,Name,Course):
        node = Node(val, priority,Name,Course)
        if not self.rear:
            self.front = self.rear = node
            return
        if self.front.priority >= node.priority:
            node.next = self.front
            self.front = node
            return
        prev = None
        cur = self.front
        while(cur and node.priority >= cur.priority):
            prev = cur
            cur = cur.next
        if not cur:
            self.rear.next = node
            self.rear = node
            
        else:
            prev.next = node
            node.next = cur
            
    def pop(self):
        if self.isEmpty():
            print('No more students to retrieve')
            return
        ptr = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        print(ptr.val,ptr.Name,ptr.Course,ptr.priority)
        return ptr.val

def add(students,val, priority,Name,Course):
    students.push(val, priority,Name,Course)

def retrieve(students):
    students.pop()

if __name__ == "__main__":
    students = PriorityQueue()
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
            add(students,Number,Number,Name,Course)
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
