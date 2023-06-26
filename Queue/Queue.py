#Queue_using_linked_list

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class queue:
    def __init__(self):
        self.head=None
    def enqueue(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
    def dequeue(self):
        
        temp=self.head
        if temp!=None:
            
            self.head=temp.next
            temp.next=None
        else:
            print("No Element exist")
                    
    def display(self):
        temp=self.head
        if temp!=None:  
            while temp!=None:
                print(temp.data,end="")
                if temp.next!=None:
                    print("-->",end="")
                temp=temp.next
        else:
            print("\n","Queue Empty")
        
obj=queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.display()
obj.dequeue()
obj.dequeue()
obj.dequeue()
print("\n","After dequeuing all the elements")
obj.display()