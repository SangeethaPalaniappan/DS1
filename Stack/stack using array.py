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

def pop(arr):
    s=len(arr)
    if s==0:
        print("List Empty")
        return arr
   
    else:    
        i=0
        a=[]
        while i!=s-1:
            Append(a,arr[i])
            i+=1
        return a

def search(n,val):
   for x in range(n):
      if arr[x]==val:
         print("Element Found")
         break
   else:
     print("No element found")
                    
def stack_append(n,b):
    for i in range(n):
        s=int(input("s:"))
        Append(b,s)
    return b
    
def stack_pop(b):  
   for x in range(n):
      b=pop(b)
   return b
     
n=int(input("n:"))
arr=[]
arr=stack_append(n,arr)
search(n,50)
search(n,40)
arr=stack_pop(arr)
if len(arr)==0:
   print("List becomes empty")
else:
   print(arr)
