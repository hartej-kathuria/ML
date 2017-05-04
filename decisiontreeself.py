import numpy as np

def entropy(y):
	p=0
	n=0
	for i in y:
		if i==0:
			n+=1
		else:
			p+=1
	sum=len(y)
	pr=p/sum
	nr=n/sum
	if (nr==0 and pr==0):
		return 0
	elif (nr == 0):
		return (-pr*np.log2(pr))
	elif (pr == 0):
		return (-nr*np.log2(nr))
	else:
		return(-pr*np.log2(pr)-nr*np.log2(nr))

def decision_tree(x,y,label):
	en=entropy(y)
	fy=np.unique(y)
	enx=[]		
	for i in x:
		fx=np.unique(i)
		enxs=en
		xcy=[]
		for j in fx:
			ysubset=[]
			for k in range(len(i)):
				if i[k]==j:
					ysubset.append(y[k])
			#print(entropy(ysubset))
			enxs=enxs-(len(ysubset)/len(y))*entropy(ysubset)			
		enx.append(enxs)
	return(best_attribute(enx,label))

def best_attribute(enx,label):
	max=0
	i=0
	for j in range(len(enx)):
		if max<enx[j]:
			max=enx[j]
			i=j
	return(label.pop(i))

#def partition():

x1 = [0,0,1,2,2,2,1,0,0,2,0,1,1,2]
x2 = [0,0,0,1,2,2,2,1,2,1,1,1,0,1]
x3 = [0,0,0,0,1,1,1,0,1,1,1,0,1,0]
x4 = [0,1,0,0,0,1,1,0,0,0,1,1,0,1]
y = [0,0,1,1,1,0,1,0,1,1,1,1,1,0]
label=["x1","x2","x3","x4"]

x=[x1,x2,x3,x4]
print(decision_tree(x,y,label))