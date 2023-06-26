#Append in Array 

def Append(arr,val):
    
    if len(arr)==0:
        for i in range(len(arr)+1):
            
            arr+=[val] 
        
        
    else:
        for i in range(len(arr)):
            
            if i==len(arr)-1:
               arr+=[val] 

#Insert

def insert(arr,pos,ele):
    b=['']
    d=a+b

    c=len(d)
    print(c)
    s=len(d)-1
    if n>=c:
        print("Cannot add element")
    else:
        for i in range(n+1,s+1):
            d[s]=d[s-1]
            print(d[s])
            s-=1
        d[n]=e
        print(d)

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
                for x in range(n,s):
                    if x!=s-1:
                        arr[x]=arr[x+1]
                        
                      
                    else:
                        a=[]
                        i=0
                        while i!=s-1:
                            Append(a,arr[i])
                            i+=1
                        print(a)
                        
#remove
#should work on it
def remove(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            delete(arr,i)
            break
    else:
        print("No element in the list")
        
#Pop

def pop(arr):
    s=len(arr)
    if s==0:
        print("List Empty")
   
    else:    
        r=arr[0:s-2]
        print(r)
                        
                           
        




a=[]
Append(a,10)
Append(a,20)
Append(a,30)
Append(a,40)
print(a)
n=int(input("Pos:"))
e=int(input("ele:"))
a.insert(n,e)
print(a)
pos=int(input("pos:"))
delete(a,pos)
print("pop:")
pop(a)
print("remove:")
val=int(input("val"))
remove(a,val)
