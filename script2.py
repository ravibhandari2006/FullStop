#!/usr/bin/python
import csv
import sys
import math

def mean(values):
	return sum(values)*1.0/len(values)

def stanDev(values):
	length=len(values)
	m=mean(values)
	total_sum=0
	for i in range(length):
		total_sum+=(values[i]-m)**2
	return math.sqrt(total_sum*1.0/length)

def process(values):
	outlier=0
	length=len(values)
	m=mean(values)
	std=stanDev(values)
	x1=m-std
	x2=m+std
	#print("dddd "+str(x1)+" dddd "+str(x2))
	for i in range(length):
		if((values[i]<x1)or(values[i]>x2)):
			outlier=1
			#print("fff "+str(values[i]))
			values[i]=m
	#if(outlier==0):
	return values
	#else:
	#	process(values)


arg1=sys.argv[1]
framewindow=sys.argv[2]
thresh=float(sys.argv[3])

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
		if(ctr>=int(framewindow)): 
			#print(str(mean(val))+" "+str(stanDev(val)))
			mu=mean(val)
			if(mu<=thresh):
				for i in range(len(val)):
					print(frames[i]+" "+str(0))
			else:
				for i in range(len(val)):
					print(frames[i]+" "+str(1))
			ctr=0
			val=[]
			frames=[]	
	if(ctr>0):
		mu=mean(val)
		if(mu<=thresh):
			for i in range(len(val)):
				print(frames[i]+" "+str(0))
		else:
			for i in range(len(val)):
				print(frames[i]+" "+str(1))
		ctr=0
		val=[]
		frames=[]		
