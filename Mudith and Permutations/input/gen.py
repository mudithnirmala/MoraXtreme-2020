import os
outCount=0
    
for count in range(10,30):
    src ="1_" + str(count)+ ".txt" 
    #src ="subtask_1_" + str(count) + ".txt"
    dst ='input'+str(count+2)+ ".txt" 
          
    # rename() function will 
    # rename all the files 
    os.rename(src, dst)

    outCount+=1
