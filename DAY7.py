
def numways(s,l):
    if l==0 or (l==1 and s[0]=='0'):
        return 0;
    return getnumways(s,l)
    
def getnumways(s, l):
    if l==0 or l==1:
        return 1
    get_ways=0
    if s[l-1]>'0':
        get_ways=getnumways(s,l-1)
    
    if s[l-2]=='1' or (s[l-2]=='2' and s[l-1]<'7'):
        get_ways +=getnumways(s,l-2)
        
    return get_ways


s=input("input the message: ")
l=len(s)
print(numways(s,l))

