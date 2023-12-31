#Linked_list
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def addfirst(self,val):
        newnode=Node(val)
        if self.head==None:#if the list is empty
            self.head=newnode
        else:
            temp=self.head
            newnode.next=temp
            self.head=newnode
    def addlast(self,val):
        newnode=Node(val)
        temp=self.head
        if self.head==None:#if the list is empty
            self.head=newnode
        else:
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
    def atposition(self,val,pos):
        newnode=Node(val)
        temp=self.head
        for i in range(pos-1): # even if the iterations are lesser than the position,
                              #temp will be assigned to next
            
            if temp==None:
               print("Index out of range")
               break
            
            temp=temp.next 
            # For each iterations temp will be assigned to next node, 
            # When the loop failed before the actual position given temp will point the actual positions previous node 
        if temp!=None:       
           newnode.next=temp.next
           temp.next=newnode
    def delete(self,key):
        temp=self.head
        if self.head==None:#if the list is empty
            print("List is Empty")
        elif temp.data==key:#The key in the head
            self.head=temp.next
            temp.next=None
        else:
            while temp.next!=None:
                if temp.next.data==key:
                     temp.next=temp.next.next
                temp=temp.next
            else:
                print("No key Exist")
    def search(self,key):
        temp=self.head
        if temp==None:
            print("No list exist")
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
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        
        print("None")
obj=linked_list()
obj.addfirst(20)
obj.addfirst(10)
obj.addlast(30)
obj.atposition(40,5)
obj.atposition(40,2)
obj.atposition(70,3)
obj.addlast(50)
obj.delete(10)
obj.delete(100)
obj.search(50)
obj.search(30)
obj.display()
