"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

"""



def clockwise_spiral(m,n, arr):
    r=0
    c=0
    
    while(r<m and c<n):
        
        
        for i in range(c,n):
            print(arr[r][i])
        r+=1
    
    
        for i in range(r,m):
            print(arr[i][m-1])
        n-=1
        
    
        for i in range(n-1,c-1,-1):
            print(arr[m-1][i])
        m-=1
            
        
        for i in range(m-1,r-1,-1):
            print(arr[i][c])
        c+=1
        
        
        
"""arr= [[1,  2,  3,  4,  5],
      [6,  7,  8,  9,  10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20]]
     
     
clockwise_spiral(4,5,arr)"""