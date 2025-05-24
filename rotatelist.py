#rotate list
class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None
def rotate(l,k):
  #length
  temp=l
  len=1
  while temp.next!=None:
    len+=1
    temp=temp.next

  k=k%len
  if k==0:
    return l

  #findlastnode to link circular
  temp.next=l
  
  newtail=l
  #break connection n-k
  for _ in range(len-k-1):
    newtail=newtail.next
  
  
  newhead=newtail.next
  newtail.next=None
  return newhead
  
def printlist(head):
  temp=head
  while temp:
    print(temp.data)
    temp=temp.next



l1=Node(1)
l1.next=Node(2)
l1.next.next=Node(3)
l1.next.next.next=Node(4)
l1.next.next.next.next=Node(5)
k=2
printlist(rotate(l1,k))




