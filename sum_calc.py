#!/usr/bin/python
import csv
import sys


arg1=sys.argv[1]
total_tp=0
total_fp=0
total_tn=0
total_fn=0
flag1=1
flag2=0
flag3=0
with open(arg1,'rb') as csvfile:
	reader1=csv.reader(csvfile,delimiter=' ')
	for row in reader1:
		total_tp+=int(row[0])		
		total_fn+=int(row[1])
		total_fp+=int(row[2])
		total_tn+=int(row[3])
	if((total_fp+total_tn)==0):
		flag2=1
		flag1=0
	if((total_fn+total_tp)==0):
		flag3=1
		flag1=0	
	#print("TP="+str(total_tp)+" FN="+str(total_fn)+" FP="+str(total_fp)+" TN="+str(total_tn))
	#print("FPR="+str(total_fp*1.0/(total_fp+total_tn))+" FNR="+str(total_fn*1.0/(total_fn+total_tp)))
	if(flag2 and flag3):
		print("undefined undefined")
	elif(flag2):
		print("undefined"+" "+str(total_fn*1.0/(total_fn+total_tp)))
	elif(flag3):
		print(str(total_fp*1.0/(total_fp+total_tn))+" undefined")
	else:
		print(str(total_fp*1.0/(total_fp+total_tn))+" "+str(total_fn*1.0/(total_fn+total_tp)))
