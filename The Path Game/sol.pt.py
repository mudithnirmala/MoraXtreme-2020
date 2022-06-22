N,K = map(int,input().strip().split())
grid = input().strip()

N+=1
inf =100000000

dp =[inf]*10001
last =[0]*10001

dp[0]=0

print(len(grid))

for i in range(1,N):
    if(grid[i]=='1'): continue
        
    for j in range(max(0,i-K),i):
        cout<<i<<' '<<j<<endl;
        if(dp[j]<inf and dp[j]+1 <dp[i]):
            dp[i]=dp[j]+1
            last[i]=j

#print(dp)
if(dp[N-1]==inf): print(-1)
else:
    #print(dp[N-1])
    p=N-1
    inverseSequence=[]
    while(p!=0):
        inverseSequence.append(p-last[p])
        p=last[p]
    #print(inverseSequence)
    for i in reversed(inverseSequence):
        print(i,end=' ')
