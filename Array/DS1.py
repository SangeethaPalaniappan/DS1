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

def Insert(arr,pos,ele):
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
        return d

#delete

def Delete(arr,n):
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
                        f=arr[0:s-1]
                        return f
                        
#remove

def remove(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            t=Delete(arr,i)
            return t
            break
    else:
        print("No element in the list")
        
#Pop

def pop(arr):
    s=len(arr)
    if s==0:
        print("List Empty")
   
    else:    
        r=Delete(arr,s-1) #this is not efficient way
        return r                        
                           
a=[]
Append(a,10)
Append(a,20)
Append(a,30)
Append(a,40)
print(a)
n=int(input("Pos:"))
e=int(input("ele:"))
a=Insert(a,n,e)
print(a)

pos=int(input("pos:"))
a=Delete(a,pos)
print(a)
print("pop:")
a=pop(a)
print(a)
print("remove:")
val=int(input("val"))
a=remove(a,val)
print(a)