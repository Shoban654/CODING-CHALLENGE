"""
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

"""


class queue:
    
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def enqueue(self,x):
        
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
        self.s1.append(x)
        
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    
    def dequeue(self):
        
        if len(self.s1)==0:
            print("queue is empyt")
            
        d=self.s1[-1]
        self.s1.pop()
        return d



if __name__=='__main__':
    n=int(input("enter the number of elements in the queue"));
    
    q=queue()
    
    for i in range(n):
        a=int(input())
        q.enqueue(a)
    
    for i in range(n):
        print(q.dequeue())
        
        
        
