#stack_using_linked_list
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,val):
        newnode=Node(val)
        if self.top==None:
            self.top=newnode
        else:
            temp=self.top
            newnode.next=temp
            self.top=newnode
    def pop(self):
        temp=self.top
        if temp!=None:
            
            self.top=temp.next
            temp.next=None
        else:
            print("No Element exist")
        
    def display(self):
        temp=self.top
        if temp!=None:  
            while temp!=None:
                print(temp.data)
                temp=temp.next
                
            
        else:
            print("Stack Empty")
    
   def search(self,val):
       temp=self.head
       while temp!=None:
          if temp.data==val:
             print("Element found")
             break        
                 
          temp=temp.next   
       else:
             print("No element found")      
               
obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.display()
obj.search(30)
obj.search(50)
obj.pop()
obj.pop()
print("After popping:")
obj.display()
print("sangeetha")
