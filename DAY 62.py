
def count(N,M):
    dp=[[0 for x in range(N)] for y in range(M)]
    
    for i in range(N):
        dp[i][0]=1;
    
    for j in range(M):
        dp[0][j]=1;
        
    for i in range(1,N):
        for j in range(1,M):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
            
    return dp[N-1][M-1]
    
    

N=int(input("enter the number of rows: "))
M=int(input("enter the number of columns: "))
print(count(N,M))