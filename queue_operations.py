#In Python, a queue is a data structure that follows the First In, First Out (FIFO) principle.
#using list,fixed length queue using list,using ll
#exmples : printer,task schedulings
#queue full or not
#single element
#more than one element

class Queue:
    def __init__(self):
        self.queue=[]
        
    def isEmpty(self):
        return len(self.queue)==0
    
    def enqueue(self,ele):
        self.queue.append(ele)
    
    def dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
        return self.queue.pop(0)
    def getRear(self):
        return self.queue[-1]
    def getFront(self):
        return self.queue[0]
    def display(self):
        if self.isEmpty():
            print("Empty")
            return
        return self.queue

ob=Queue()
ob.enqueue(100)
ob.enqueue(200)
ob.enqueue(300)
print(ob.display())
ob.dequeue()
print(ob.display())
print("Rear ele: " ,ob.getRear())
print("Front ele: " ,ob.getFront())
print("queue : ",ob.display())
print("is empty :",ob.isEmpty())


    