#Queue_using_array

#Append

def Append(arr,val):
    
    if len(arr)==0:
        for i in range(1):
            #s=int(input("s:"))
            arr+=[val] 
            
        
        
    else:
        for i in range(len(arr)):
            #s=int(input("s:"))
            if i==len(arr)-1:
               arr+=[val] 
 
#delete

def delete(arr,n):#here used delete because the position of each element changes
    s=len(arr)
    if s==0:
        print("List Empty")
        
    elif n>=s:
        print("index out of range")
        return a
    else:    
        for i in range(s):
            if n==i:                
                while n!=s-1:
                    arr[n]=arr[n+1]
                    n+=1
                      
                else:
                    a=[]
                    i=0
                    while i!=s-1:
                        Append(a,arr[i])
                        i+=1
                    print(a)
                    return a
                    break
                        
def search(n,val):
   for x in range(n):
      if arr[x]==val:
         print("Element Found")
         break
   else:
     print("No element found")                     

class Enqueue:
    def __init__(self):
        self.front=-1
        self.rear=-1
    def Queue_enqueue(self,n,b):#n is the size of the Queue
        b=n*[-1]
        while n-1!=-1:
            s=int(input("s:"))#the elements to be added
            if self.front==-1:
                self.front=0
                b[self.front]=s
            self.rear+=1
            b[self.rear]=s  #changing the position 
            n-=1
            print(b)
        return b

    def Queue_dequeue(self,b):
        s=delete(b,0)
        r=self.rear
        self.rear=r-1
        
            
        if self.rear==-1:#if therer is no element
            self.front=-1
            print("Empty Queue")
        return s
     
n=5
arr=[]
a=Enqueue()
arr=a.Queue_enqueue(n,arr)
val=int(input())
search(n,val)
arr=a.Queue_dequeue(arr)
arr=a.Queue_dequeue(arr)
arr=a.Queue_dequeue(arr)
arr=a.Queue_dequeue(arr)
arr=a.Queue_dequeue(arr)
