#!/usr/bin/python
import numpy as np
from sklearn import svm
from sklearn import tree
#from sklearn import cross_validation
import csv
import sys

arg1=sys.argv[1]
arg2=sys.argv[2]
#fo=open("vm_time.txt","w")
X_train=[]
Y_train=[]
X_test=[]
Y_test=[]
tempList=[]
clf=svm.SVC(kernel='linear',C=1.0)
#clf = tree.DecisionTreeClassifier()
with open(arg1,'rb') as csvfile:
	reader=csv.reader(csvfile,delimiter=' ')
	for row in reader:
		#tempList.append([float(row[0]),float(row[1]),float(row[4])])
		tempList.append([float(row[0]),float(row[4])])
		Y_train.append(int(row[5]))
	X_train=np.asarray(tempList)
	clf.fit(X_train,Y_train)

tempList=[]
timelist=[]
with open(arg2,'rb') as csvfile:
	reader1=csv.reader(csvfile,delimiter=' ')
	for row in reader1:
		#tempList.append([float(row[0]),float(row[1]),float(row[4])])
		tempList.append([float(row[0]),float(row[4])])
		#timelist.append(row[7])
		Y_test.append(int(row[5]))
	X_test=np.asarray(tempList)
temp=clf.predict(X_test)
i=0
tp=0
fn=0
fp=0
tn=0
while(i<len(temp)):
	val1=Y_test[i] #groundtruth
	val2=temp[i]   #predicted
	if((val1==0)and(val2==0)):
		tp+=1
	if((val1==0)and(val2==1)):
		fn+=1
		#fo.write("FN,"+str(int(timelist[i]))+","+str(int(timelist[i])-prev_fneg_time)+"\n")	
		#prev_fneg_time=int(timelist[i])
	if((val1==1)and(val2==0)):
		fp+=1
		#fo.write("FP,"+str(int(timelist[i]))+","+str(int(timelist[i])-prev_fpos_time)+"\n")	
		#prev_fpos_time=int(timelist[i])
	if((val1==1)and(val2==1)):
		tn+=1
	i=i+1
print("TP="+str(tp)+" FN="+str(fn)+" FP="+str(fp)+" TN="+str(tn)+" FPR="+str(fp*1.0/(fp+tn))+" FNR="+str(fn*1.0/(tp+fn))+" Score="+str(clf.score(X_test,Y_test)))
#print("TP="+str(tp)+" FN="+str(fn)+" FP="+str(fp)+" TN="+str(tn))
#print(clf.score(X_test,Y_test))
#fo.close()

