import os
outCount=13
    
for count in range(3,10):
    src ="01-handmade-0" + str(count)
    #src ="subtask_1_" + str(count) + ".txt"
    dst ='output0'+str(count)+ ".txt" 
          
    # rename() function will 
    # rename all the files 
    os.rename(src, dst)

    outCount+=1
