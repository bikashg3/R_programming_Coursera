#import pandas as pd 
#import numpy as np 

import os
path1 = '/home/bikash/Desktop/Training_SmartJoules/Files/logs/Chiller/'
#path1 = '/home/bikash/Desktop/Training_SmartJoules/Files/logs/NF29/'
output_path = '/home/bikash/Desktop/Training_SmartJoules/Files/logs/python functions/merged_files/'
output_filename='/home/bikash/Desktop/Training_SmartJoules/Files/logs/output_Chiller-file.txt'


def fileExtract():
    import glob, os
    global filenames_
    filenames_=[]
    os.chdir(path1)
    for file in glob.glob("*.txt"):
        #print(file)
        filenames_.append(file)
    #print(sorted(filenames_))    
    return(filenames_)    
    

fileExtract()





def main(input_filenames):
    '''Main function'''
    #input_filenames = ['a', 'b', 'c']

    block_size = 2048 * 2048
    if hasattr(os, 'O_BINARY'):
        o_binary = getattr(os, 'O_BINARY')
    else:
        o_binary = 0
    f=open(output_filename,"w+")
    f.close()
    output_file = os.open(output_filename, os.O_WRONLY | o_binary)
    for input_filename in input_filenames:
        if os.path.exists(path1+input_filename):
            input_file = os.open(path1+input_filename, os.O_RDONLY | o_binary)
            #print(path1+input_filename+'.txt')
            while True:
                input_block = os.read(input_file, block_size)
                if not input_block:
                        #print("break ho gya")
                    break
                    continue
                os.write(output_file, input_block)
            os.close(input_file)
   
    os.close(output_file)

            
main(filenames_)
 
#print(filenames_) 