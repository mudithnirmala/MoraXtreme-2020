import random


for t in range(10,11):
    file_name = "input0"+str(t)+".txt"

    with open(file_name,'w+') as f:
       # N=random.randint(90000,100000)
       # M=random.randint(5000,50000)
        N=10000
        M=1000
        A=""
        B=""

        for i in range(N):
            x = random.randint(0,26)

            c = chr(ord('A')+x)
            A+=c

        for i in range(M):
            x = random.randint(0,20)

            c = chr(ord('A')+x)
            B+=c

        #B+=A[M:M+1000]
        f.write(A+'\n')
        f.write(B+'\n')
        f.close()
