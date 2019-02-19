#!/usr/bin/python
import sys
import csv

#Usage: ./compare.py gt_myvideo1_cut1.txt thresh_myvideo1_cut_30_50.txt
file1=sys.argv[1] #file1
file2=sys.argv[2] #file2
w=int(sys.argv[3]) #Win Size
fo1=open(file1,"r")
fo2=open(file2,"r")
flag=1 #flag=0 means stop reading from either of the files
line1=""
line2=""
val1=0
val2=0
tp=0
fn=0
fp=0
tn=0
while(flag):
	line1=fo1.readline()
	line2=fo2.readline()
	if(line1!=""):
		val1=int(line1.split(' ')[1])
	else:
		flag=0

	if(line2!=""):
		val2=int(line2.split(' ')[1])		
	else:
		flag=0
	
	if((val1==0) and (val2==0)):
		tp+=1
	elif((val1==0) and (val2==1)):
		fn+=1
	elif((val1==1) and (val2==0)):
		fp+=1
	else:
		tn+=1
#print TP FN FP TN
print(str(tp/w)+" "+str(fn/w)+" "+str(fp/w)+" "+str(tn/w))
	
