#!/usr/bin/python
import csv
import sys
import math	

arg1=sys.argv[1]
framewindow=int(sys.argv[2])

def max_vote(values):
	if(sum(values)<(framewindow/2)):
		return 0
	else:
		return 1
ctr=0
frames=[]
val=[]
with open(arg1,'rb') as csvfile:
	reader1=csv.reader(csvfile,delimiter=' ')
	ctr=0
	mu=0.0
	for row in reader1:
		ctr=ctr+1
		frames.append(row[0])
		val.append(float(row[1])) #make the list
		if(ctr>=framewindow): 
			if(max_vote(val)):
				for i in range(len(val)):
					print(frames[i]+" "+str(1))
			else:
				for i in range(len(val)):
					print(frames[i]+" "+str(0))
			ctr=0
			val=[]
			frames=[]	
	if(ctr>0):
		if(max_vote(val)):
			for i in range(len(val)):
				print(frames[i]+" "+str(1))
		else:
			for i in range(len(val)):
				print(frames[i]+" "+str(0))
		ctr=0
		val=[]
		frames=[]		
