from collections import deque
class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
    def __repr__(self):
        return f"Student({self.roll}, '{self.name}')"
s = deque()
s.append(Student(1, "Priya"))
s.append(Student(2, "Sriya"))
print(s)
print(s[-1])
print(s.pop())
print(s)
