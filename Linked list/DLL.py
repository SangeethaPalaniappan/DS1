#Double linked_list
class Node:
   def __init__(self,val):
      self.prev=None
      self.data=val
      self.next=None
class dlinked_list:
    def __init__(self):
        self.head=None
    def addfirst(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            newnode.next=temp
            temp.prev=newnode
            self.head=newnode
    def addlast(self,val):
        newnode=Node(val)
        temp=self.head
        if self.head==None:
            self.head=newnode
        else:
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
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
            print("List is Empty")
        elif temp.data==key:
            self.head=temp.next
            temp.next=None
            self.head.prev=None
        else:
            while temp.next!=None:
               
               if temp.next.data==key:
                    temp.next=temp.next.next
                    temp.next.prev=temp
               temp=temp.next
            else:
               print("No key exist")    
            
    def search(self,key):
        temp=self.head
        if self.head==None:
            print("No element exist")
        else:
            while temp!=None:
                if temp.data==key:
                   print("Key Found")
                   break
                temp=temp.next
            else:
                print("Key Not Found")
    def display(self):
        temp=self.head
        print("None"," <--> ",end="")
        while temp!=None:
            print(temp.data," <--> ",end="")
            temp=temp.next
        print("None")
obj=dlinked_list()
obj.addlast(20)
obj.addfirst(10)
obj.addlast(30)
obj.addlast(50)
obj.atposition(40,2)
obj.search(500)
obj.delete(400)
obj.display()