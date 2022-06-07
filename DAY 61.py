def power(x, y):
    if y==0:
        return 1;
    if x==0:
        return 0;
    return x*power(x,y-1)
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
print(power(x,y))