#Should work on it
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
   
    else:    
        i=0
        a=[]
        while i!=s-1:
            Append(a,arr[i])
            i+=1
        print(a)
                     
def stack_append(n,b):
    for i in range(n):
        s=int(input("s:"))
        Append(b,s)
    print(b)
    
def stack_pop(b):    
    for i in range(1):
        print(pop(b))

def search(n,val):
   for x in range(n):
      if arr[x]==val:
         print("Element Found")
         break
      else:
         print("No element found")
         break        
     
n=int(input("n:"))
arr=[]
stack_append(n,arr)
stack_pop(arr)