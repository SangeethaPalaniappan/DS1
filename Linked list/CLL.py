#Circular linked_list
class Node:
   def __init__(self,val):
      self.prev=None
      self.data=val
      self.next=None
class clinked_list:
    def __init__(self):
        self.head=None
    def addfirst(self,val):
        newnode=Node(val)
        
        if self.head==None:
            
            newnode.next=newnode
            newnode.prev=newnode
            self.head=newnode
            
            
        else:
            temp=self.head
            newnode.next=temp
            newnode.prev=temp.prev
            temp.prev.next=newnode
            temp.prev=newnode
            self.head=newnode
            
    def addlast(self,val):
        newnode=Node(val)
        temp=self.head
        if temp==None:
            newnode.next=newnode
            newnode.prev=newnode
            self.head=newnode
        else:
            while temp.next!=self.head:
                temp=temp.next
            newnode.next=temp.next
            newnode.prev=temp
            temp.next.prev=newnode
            temp.next=newnode
            
    def atposition(self,val,pos):
        newnode=Node(val)
        temp=self.head
        for i in range(pos):
            temp=temp.next
        temp.next.prev=newnode
        newnode.next=temp.next
        newnode.prev=temp   
        temp.next=newnode
    def delete(self,key):
        temp=self.head
        if self.head==None:
            print("\n","List is Empty")
        elif temp.data==key:
            temp.next.prev=temp.prev
            temp.prev.next=temp.next
            self.head=temp.next
            temp.next=None
            temp.prev=None
            
        else:
            while temp.next!=self.head:
               if temp.next.data==key:
                    temp.next=temp.next.next
                    temp.next.prev=temp
                    break 
               temp=temp.next
            else:
               print("\n","No key exist")    
            
    def search(self,key):
        temp=self.head
        if temp==None:
            print("No element exist")
        elif temp.data==key:
            print("\n","Key Found")
        else:    
            Next=self.head.next   
            while Next!=self.head:
                if Next.data==key:
                   print("\n","Key Found")
                   break
                Next=Next.next
            else:
                print("\n","Key Not Found")
    def display(self):
        temp=self.head
        Next=self.head.next
        print(" <--> ",temp.data," <--> ",end="")
        while Next!=self.head:
            print(Next.data," <--> ",end="")
            Next=Next.next
        
obj=clinked_list()
obj.addlast(20)
obj.addfirst(10)
obj.addlast(30)
obj.addlast(50)
obj.atposition(40,2)
obj.display()  
obj.search(50)
obj.search(500)
obj.delete(40)
obj.delete(400)
obj.display()