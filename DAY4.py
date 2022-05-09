def smallint(a,n):
    for i in range(1,n+2):
        flag=False
        for j in range(n):
            if a[j]==i:
                flag=True
                break
        if flag==False:
            return i
        
a=[]
n=int(input("enter the number of elements in array:"))
for i in range(n):
    l=int(input())
    a.append(l)
print(smallint(a,n))