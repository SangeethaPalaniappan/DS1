#should work on it
#stack_using_linked_list
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            newnode.next=temp
            self.head=newnode
    def pop(self):
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
                print(temp.data)
                temp=temp.next
                
            
        else:
            print("Stack Empty")
        
obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.display()
obj.pop()
obj.pop()
print("\n","After popping:")
obj.display()
print("sangeetha")