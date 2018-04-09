import time
import datetime

filename = datetime.datetime.now()
filedata = []
for i in range(1,4):
    with open("file"+str(i)+".txt") as fh:
        filedata.append(fh.read())

#file = open(filename.strftime("%Y %M %D-%H")+".txt",'w+')
file = open(filename.strftime("%Y %B %-d %H-%M-%S")+".txt",'w+')
for i in filedata:
    file.write(i+"\n")
file.close()
