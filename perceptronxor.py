import numpy as np
def actfun(y):
	if y<0:
		return 0
	else:
		return 1

def activationfunct(net):
	y=1/(1+np.exp(-net))
	return y

def weightupdate(d,w,bias,ox1,ox2,l,e):
	w4o=w[4]
	w5o=w[5]
	w[4]=w[4]+ox1*l*e
	w[5]=w[5]+ox1*l*e
	bias[2]=bias[2]+l*e
	w[0]=w[0]+d[0]*l*e*w4o
	w[2]=w[2]+d[0]*l*e*w4o
	w[1]=w[1]+d[1]*l*e*w5o
	w[3]=w[3]+d[1]*l*e*w5o
	bias[1]=bias[1]+l*e*w4o
	bias[2]=bias[2]+l*e*w4o
	return w,bias 


def nn(data,w,bias,l):
	for d in data:
		x1=d[0]*w[0]+d[1]*w[1]+bias[0]
		x2=d[0]*w[2]+d[1]*w[3]+bias[1]
		ox1=actfun(x1)
		ox2=actfun(x2)
		yobv=ox1*w[4]+ox2*w[5]+bias[2]
		if yobv!=d[2]:
			w,bias=weightupdate(d,w,bias,ox1,ox2,l,(yobv-d[2]))
	return w,bias

data=[[0,0,0],[0,1,1],[1,0,1],[1,1,0]]
bias=[1,1,1]
w=[0.6,0.6,1.1,1.1,-2,1.1]
n=5
l=0.1
for i in range(n):
	w,bias=nn(data,w,bias,l)
print(w,bias)