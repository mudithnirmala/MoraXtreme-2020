import random

H=1000000000
W=1000000000

for t in range(20,30):
    file_name = "input"+str(t)+".txt"

    with open(file_name,'w+') as f:
        T = 20
        
        f.write(str(T)+' '+str(H)+' '+str(W)+'\n')

        for t in range(T):
            N = 1000
            R = random.randint(100000,3000000)

            f.write(str(N)+' '+str(R)+'\n')

            for i in range(N):
                x = random.randint(0,W)
                if(i!=N-1): f.write(str(x)+' ')
                else: f.write(str(x)+'\n')
                
                
            for i in range(N):
                y = random.randint(0,H)
                if(i!=N-1): f.write(str(y)+' ')
                else: f.write(str(y)+'\n')
                
