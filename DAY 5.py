def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair
def car(pair):
    return pair(lambda a,b:a)
def cdr(pair):
    return pair(lambda a,b:b)
        

a=int(input("enter the first element: "))
b=int(input("enter the seconde element: "))
print(car(cons(a,b)))
print(cdr(cons(a,b)))