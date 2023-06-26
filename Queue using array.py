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

def delete(arr,n):
    s=len(arr)
    if s==0:
        print("List Empty")
    elif n>=s:
        print("index out of range")
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
                    break
                        
                     

def Queue_enqueue(n,b):
      for i in range(n):
       s=3
       Append(b,s)
      print(b)

def Queue_dequeue(b):
    
    print(delete(b,0))
     
n=1
arr=[10,20,30,40]

Queue_dequeue(arr)