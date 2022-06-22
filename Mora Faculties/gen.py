import os
outCount=13
    
for count in range(10,17):
    #src ="sample_0" + str(count) + ".txt"
    src ="subtask_1_" + str(count) + ".txt"
    dst ='output0'+str(outCount)+ ".txt" 
          
    # rename() function will 
    # rename all the files 
    os.rename(src, dst)

    outCount+=1
