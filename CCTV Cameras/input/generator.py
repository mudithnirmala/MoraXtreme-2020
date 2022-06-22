import random

H=1000000000
W=1000000000

for t in range(10,30):
    file_name = "input"+str(t)+".txt"

    with open(file_name,'w+') as f:
        T = 20
        
        f.write(str(T)+' '+str(H)+' '+str(W)+'\n')

        for t in range(T):
            N = random.randint(800,1000)
            R = random.randint(100000,50000000)

            f.write(str(N)+' '+str(R)+'\n')

            for i in range(N):
                x = random.randint(1,W)
                if(i!=N-1): f.write(str(x)+' ')
                else: f.write(str(x)+'\n')
                
                
            for i in range(N):
                y = random.randint(1,H)
                if(i!=N-1): f.write(str(y)+' ')
                else: f.write(str(y)+'\n')
                
