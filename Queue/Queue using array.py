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
                        
                     

def Queue_enqueue(n,b):#n is the size of the Queue
      for i in range(n):
        s=int(input("s:"))#the elements to be added
        Append(b,s)
      print(b)
      return b

def Queue_dequeue(b):
    s=delete(b,0)
    return s
     
n=5
arr=[]
arr=Queue_enqueue(n,arr)
arr=Queue_dequeue(arr)
arr=Queue_dequeue(arr)
