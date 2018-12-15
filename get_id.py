import os

# create the list containing all files from the current dir
filelistall = os.listdir(os.getcwd())

# create the list containing only data files end with ".txt" 
filelist = filter(lambda x: x.endswith('.txt'), filelistall)


all_text = []
all_ids = []
for filename in filelist:
    f = open(filename,"r")
    number = float(filename[8:-4])
    all_ids.append(number)
    text = ''.join(f.readlines())
    all_text.append(text)
    f.close()
