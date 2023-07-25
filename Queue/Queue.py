#Queue_using_linked_list

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class queue:
    def __init__(self):
        
        self.rear=None
        self.front=None
    def enqueue(self,val):
        newnode=Node(val)
        if self.front==None:
            self.front=newnode
            self.rear=newnode
        else:
            temp=self.front
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            self.rear=newnode
    def dequeue(self):
        
        temp=self.front
        
        #for i in range(n) - if all elements dequeue once
        if self.front==self.rear:
                self.rear=None
                self.front=None   
                temp=None
        elif temp!=None:
            self.front=temp.next
            temp.next=None
            
        else:
            print("No Element exist")
                    
    def display(self):
        temp=self.front
        if temp!=None:  
            while temp!=None:
                print(temp.data,end="")
                if temp.next!=None:
                    print("-->",end="")
                temp=temp.next
        else:
            print("Queue Empty")
            
    def search(self,val):
       temp=self.front
       while temp!=None:
          if temp.data==val:
             print("Element found")
             break        
                 
          temp=temp.next   
       else:
             print("No element found")
                          
obj=queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.search(20)
obj.search(100)
obj.display()
obj.dequeue()
obj.dequeue()
if obj.dequeue()==None:
    print("Queue becomes empty")

print("After dequeuing all the elements")
obj.display()
