from collections import deque
class cricketer:
    def __init__(self,name,run,nickname):
        self.name=name
        self.run=run
        self.nickname=nickname
    def __repr__(self):
        return f"{self.name},{self.run}"

names = ["rain", "sun", "moon", "time"]
runs = [0, 100, 20, 40]
nicknames = ["Boom", "Bam", "Vim", "Vum"]
stack=deque()
for i in range(len(names)):
    stack.append(cricketer(names[i],runs[i],nicknames[i]))
print(stack)
for i in stack:
    print(i.name)
    


    