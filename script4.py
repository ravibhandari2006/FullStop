#!/usr/bin/python
import csv
import sys
import math
import numpy as np

#Usage: ./script4.py trim_Algo*.txt trim_Acc*.txt 1 > merge_15.txt

def mean(values):
	return sum(values)*1.0/len(values)

def stanDev(values):
	#length=len(values)
	#m=mean(values)
	#total_sum=0
	#for i in range(length):
	#	total_sum+=(values[i]-m)**2
	#return math.sqrt(total_sum*1.0/length)
	tst=values
	np.asarray(tst)
	return np.std(tst)

def energy(values):
        n = len(values)
        k = np.arange(n)
        T = n/Fs
        #print T
        frq = k/T # two sides frequency range
        frq = frq[range(n/2)] # one side frequency range
        Y = np.fft.fft(values) # fft computing
        #Y = Y[range(n/2)]
        E = np.sum(abs(Y)**2)*1.0/n #Energy of the signal
        entropy = 0.0
        psd = [] #power spectral density
        p = [] #probability
        for i in range(0,n):
                psd.append((abs(Y[i])**2)*1.0/n)
        for i in range(0,n):
                p.append(psd[i]*1.0/E)
        for i in range(0,n):
		if(p[i]>0):
	                entropy += (-1.0*p[i]*np.log(p[i]))
        return E,entropy

Fs = 20.0
arg1=sys.argv[1] 
arg2=sys.argv[2] 
file1="temp1.txt"
file2="temp2.txt"
framewindow=round(float(sys.argv[3])*30)
fo1=open(file1,"w")
fo2=open(file2,"w")

val=[] #radial score
latval=[] #lateral score
AccX=[]
AccY=[]
AccZ=[]
gtval1=[]
gtval2=[]
currquotient=0
prevquotient=0

with open(arg1,'rb') as csvfile:
	reader1=csv.reader(csvfile,delimiter=' ')
	mu=0.0
	for row in reader1:
		currquotient=int(row[0])/framewindow
		if(round(currquotient) != round(prevquotient)):
			if(mean(gtval1)>0.5):
				strgt="1"
			else:
				strgt="0"
			fo1.write(str(mean(val))+" "+str(mean(latval))+" "+strgt+"\n")
			val=[]
			latval=[]
			gtval1=[]
			val.append(float(row[1])) #make the list
			latval.append(float(row[2]))
			gtval1.append(int(row[3]))
			prevquotient=currquotient
		else:
			val.append(float(row[1])) #make the list
			latval.append(float(row[2]))
			gtval1.append(int(row[3]))
currquotient=0
prevquotient=0
with open(arg2,'rb') as csvfile:
	reader2=csv.reader(csvfile,delimiter=' ')
	mu=0.0
	for row in reader2:
		currquotient=int(row[0])/framewindow
		if(round(currquotient) != round(prevquotient)):
			#print gtval2
			if(mean(gtval2)>0.5):
				strgt="1"
			else:
				strgt="0"
			energy_x,entropy_x = energy(AccX)
                        energy_y,entropy_y = energy(AccY)
                        energy_z,entropy_z = energy(AccZ)

			fo2.write(str(stanDev(AccX))+" "+str(stanDev(AccY))+" "+str(stanDev(AccZ))+" "+str(energy_x)+" "+str(entropy_x)+" "+str(energy_y)+" "+str(entropy_y)+" "+str(energy_z)+" "+str(entropy_z)+" "+strgt+"\n")
			
			AccX=[]
			AccY=[]
			AccZ=[]
			gtval2=[]
			AccX.append(float(row[1])) #make the list
			AccY.append(float(row[2]))
			AccZ.append(float(row[3]))
			gtval2.append(int(row[4]))
			prevquotient=currquotient
		else:
			AccX.append(float(row[1])) #make the list
			AccY.append(float(row[2]))
			AccZ.append(float(row[3]))
			gtval2.append(int(row[4]))


fo1.close()
fo2.close()

fo1=open(file1,"r")
fo2=open(file2,"r")
flag=1
line1=fo1.readline()
line2=fo2.readline()
printstr=""
while(flag):
	if(line1!=""):
		gtlabel=int(line1.split(' ')[2])
		printstr=line1.split(' ')[0]+" "+line1.split(' ')[1]+" "
		line1=fo1.readline()
	else:
		flag=0

	if(line2!=""):
		printstr+=line2.split(' ')[0]+" "+line2.split(' ')[1]+" "+line2.split(' ')[2]+" "+line2.split(' ')[7]+" "+line2.split(' ')[8]+" "+str(gtlabel)
		line2=fo2.readline()
	else:
		flag=0
	if(flag):
		print printstr

fo1.close()
fo2.close()
