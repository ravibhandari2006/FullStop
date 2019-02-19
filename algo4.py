#!/usr/bin/python
import csv
import sys
import math

filename=sys.argv[1]
window=int(sys.argv[2])
framerate=int(sys.argv[3])
ctr=0
if(framerate==30):
	invariant=10 #for algo1 frame rate 30
elif(framerate==15):
	invariant=11
elif(framerate==10):
	invariant=0
with open(filename,'rb') as csvfile:
	reader1=csv.reader(csvfile,delimiter=' ')
	for row in reader1:
		if(int(row[0])==window):
			ctr+=1
			if((ctr%12)==invariant):
				print(row[1]+" "+row[2]+" "+row[3])
