#stack_using_array

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

def Delete(arr,pos):
    s=len(arr)
    if s==0:
        print("List Empty")
        return arr
    elif pos>=s:
        print("index out of range")
        return arr
    else:    
        for i in range(s):
            
            #To find the position
            if pos==i:
                for x in range(pos,s):
                    
                    #replacing the value 
                    if x!=s-1:# s is the last index
                        arr[x]=arr[x+1]
                        
                      
                    else:
                        #To delete the last element, reduced the size of the list and add the elements at the last position
                        f=[]
                        for t in range(s-1):
                            Append(f,arr[t])  
                        return f

def search(n,val,arr):
   for x in range(n):
      if arr[x]==val:
         print("Element Found")
         break
   else:
     print("No element found")

class Stack:
    def __init__(self):
        self.top=-1
                    
    def stack_push(self,n,b):
        b=n*[-1]
        
        while n-1!=-1: 
           s=int(input("s:"))       
           self.top+=1
           o=self.top       
           b[o]=s      
           n-=1       
        return b

    def stack_pop(self,b):    
       while self.top!=-1:
           b=Delete(b,len(b)-1)
           self.top-=1
           if self.top==-1:
               print("Stack empty")         
       return b              
       
     
n=int(input("n:"))
arr=[]
a=Stack()
arr=a.stack_push(n,arr)
search(n,50,arr)
search(n,40,arr)
arr=a.stack_pop(arr)
