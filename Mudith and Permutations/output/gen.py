import os
outCount=0
    
for count in range(0,2):
    src ="0_0" + str(count)+ ".txt" 
    #src ="subtask_1_" + str(count) + ".txt"
    dst ='output0'+str(count)+ ".txt" 
          
    # rename() function will 
    # rename all the files 
    os.rename(src, dst)

    outCount+=1
