#!/usr/bin/python
import numpy as np
from sklearn import svm
from sklearn import tree
from sklearn.cross_validation import train_test_split
#from sklearn import cross_validation
import csv
import sys

arg1=sys.argv[1] #datafile
#fo=open("acc_time.txt","w")
X=[]
Y=[]
tempList=[]
clf=svm.SVC(kernel='linear',C=1.0)
#clf = tree.DecisionTreeClassifier()
with open(arg1,'rb') as csvfile:
	reader=csv.reader(csvfile,delimiter=' ')
	for row in reader:
		#tempList.append([float(row[0]),float(row[4])])
		tempList.append([float(row[0]),float(row[4]),float(row[5]),float(row[6])])
		Y.append(int(row[7]))
	X=np.asarray(tempList)

for i in range(0,10):
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=i)
	clf.fit(X_train,Y_train)
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
		if((val1==1)and(val2==0)):
			fp+=1
		if((val1==1)and(val2==1)):
			tn+=1
		i=i+1
	#print("TP="+str(tp)+" FN="+str(fn)+" FP="+str(fp)+" TN="+str(tn)+" FPR="+str(fp*1.0/(fp+tn))+" FNR="+str(fn*1.0/(tp+fn))+" Score="+str(clf.score(X_test,Y_test)))
	print(str(tp)+" "+str(fn)+" "+str(fp)+" "+str(tn))
	#print(clf.score(X_test,Y_test))

