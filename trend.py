import numpy
from math import pow,sin,cos
from moje import sigmoid as sid
from random import choice
from matplotlib import pyplot as plt
	
def los():
	return numpy.random.randn()
	
def nachyl(number,target,punkt):
	dcost_dpred=2*(number-target)
	dpred_dsigm=1
	dcost_dw1=dcost_dpred*dpred_dsigm*punkt[0]
	dcost_db=dcost_dpred*dpred_dsigm
	return dcost_dw1,dcost_db
	
def zgaduj(w1,b,punkt):
	z=w1*punkt[0]+b
	return z
	
def uczenie(ile_lekcji,zestaw_nauki):
	w1=los()
	b=los()
	for i in range(ile_lekcji):
		tren=choice(zestaw_nauki)
		tar=tren[1]
		pred=zgaduj(w1,b,tren)
		bladw1,bladb=nachyl(pred,tar,tren)
		w1-=0.01*bladw1
		b-=0.01*bladb
		#if i%1000==0:print(i)
	ew1=w1
	eb=b
	return ew1,eb