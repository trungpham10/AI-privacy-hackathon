# read specific files 

# read data from text file
import os

filelistall = os.listdir(os.getcwd())

filelist = filter(lambda x: x.endswith(".txt"), filelistall)

for filename in filelist:
    #print(filename)
    f = open(filename,'r')
    content = f.readlines()
    text = ''.join(content)
#print(content)
#print(text)