#!/usr/bin/python
import numpy as np
from sklearn import svm
from sklearn import tree
from sklearn.cross_validation import train_test_split
#from sklearn import cross_validation
import csv
import sys
import time

arg1=sys.argv[1]
#fo=open("acc_time.txt","w")
X=[]
Y=[]
tempList=[]
train_time=0.0
class_time=0.0
clf=svm.SVC(kernel='linear',C=1.0)
#clf = tree.DecisionTreeClassifier()
with open(arg1,'rb') as csvfile:
	reader=csv.reader(csvfile,delimiter=' ')
	for row in reader:
		#tempList.append([float(row[0]),float(row[1])])
		tempList.append([float(row[0])])
		Y.append(int(row[2]))
	X=np.asarray(tempList)

for i in range(0,10):
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=i)
	start_time=time.time()
	clf.fit(X_train,Y_train)
	end_time=time.time()
	temp=clf.predict(X_test)
	final_end_time=time.time()
	train_time+=float(end_time - start_time)
	class_time+=float(final_end_time - end_time)
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
	print(str(tp)+" "+str(fn)+" "+str(fp)+" "+str(tn)+" "+str(fp*1.0/(fp+tn))+" "+str(fn*1.0/(tp+fn))+" "+str(train_time/10)+" "+str(class_time/10)+" "+str(clf.coef_)+" "+str(clf.intercept_))
	#print(clf.score(X_test,Y_test))

