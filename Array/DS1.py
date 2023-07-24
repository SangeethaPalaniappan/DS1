#Append in Array 
#To insert the element at the last 
def Append(arr,val):
    if len(arr)==0:
        for i in range(len(arr)+1):
            arr+=[val] #put the value into the list and adding two lists
        
        
    else:
        for i in range(len(arr)):
            
            if i==len(arr)-1:
               arr+=[val] #put the value into the list and adding two lists

#Insert
#Adding the elements at the specific position

def Insert(arr,pos,ele):
    
    #Creating new space by adding it to the array
    d=arr+['']
    c=len(d)
    print(c)
    s=len(d)-1
    
    #if the position greater than or equal to the lenght of the array then the following condition will proceed
    if pos>=c:
        print("Cannot add element")
        return arr
    
    else:
        for i in range(n+1,c):# Enough to iterate from the postion's next
            d[s]=d[s-1]
            print(d[s])
            s-=1
        d[pos]=ele
        return d

#delete
#This function is to deleting particular position

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
                        
#remove
#deleting the element 
#Find the position of the value and delete it by the Delete function

def remove(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            t=Delete(arr,i)
            return t
            break
    else:
        print("No element in the list") #If we use the print function here we should return the array 
        return arr
        
#Pop
#Deleting the last element
#Use the delete function by giving the last index as position

def pop(arr):
    s=len(arr)
    if s==0:
        print("List Empty")
        return arr
   
    else:    
        r=Delete(arr,s-1) 
        return r                        
                           
a=[]
Append(a,10)
Append(a,20)
Append(a,30)
Append(a,40)
print(a)
n=int(input("Pos:"))
e=int(input("ele:"))
a=Insert(a,n,e) #here assigning a to update the list
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
