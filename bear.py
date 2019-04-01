#Be careful! What program actually does is it cuts all unnecessery things for it leaving only data. Make sure you make backup for your file before giving it to BEAR :)
import numpy as np
from matplotlib import pyplot as plt
import trend
import math
def pobierz_punkty(x,y):
	punkty=[]
	for i in range(x,y):
		punkty.append([wydluzenie[i],naprezenie[i]])
	return punkty
def er02(x,y):
	punkty=pobierz_punkty(x,y)
	a,b=trend.uczenie(300000,punkty)
	x02=[]
	y02=[]
	mini=1
	R02=0
	for i,napr in enumerate(naprezenie):
		y02.append(napr)
		x02.append(((napr)-b)/a+0.2)
		if(math.fabs(((napr)-b)/a+0.2-wydluzenie[i])<mini):
			mini=math.fabs(((napr)-b)/a+0.2-wydluzenie[i])
			R02=napr
	return x02,y02,R02,a
def A(nachylenie):
	napr=0;
	i=0;
	while napr<Rm:
		napr=naprezenie[i]
		i+=1
	punkty=pobierz_punkty(i+1,len(naprezenie)-1)
	pop=Rm+0.2
	napr=Rm
	i=0
	while (pop-napr)<1.5:
		i+=1
		pop=punkty[i-1][1]
		napr=punkty[i][1]
		print(punkty[i-1][1],punkty[i][1])
	b=punkty[i][1]-(nachylenie*punkty[i][0])
	wynik=-b/nachylenie
	return wynik
def wykres():
	plt.plot(wydluzenie,naprezenie,color="g")
	plt.plot(x02,y02,color="r")
	plt.show()
#pobranie nazwy pliku
nazwa_pliku=input("Podaj nazwę pliku (z rozszerzeniem!): ")
#czy jest potrzeba czyścić
f = open(nazwa_pliku,"r")
linia=f.readline()
try: liczba=int(linia[0])
except: liczba="a"
f.close
#oczyszczenie pliku ze zbędnych danych
if(type(liczba)!=int):
	f = open(nazwa_pliku+".xls","r")
	lines=f.readlines()
	f.close()
	f = open(nazwa_pliku+".xls","w")
	for i,line in enumerate(lines):
		if i>40:
			f.write(line)
	for i in range(50):
		f.write("\n")
	f.close()
#pobranie danych do programu
czas,wydluzenie,sila,naprezenie,liczba_cykli,c_liczba_cykli,powtorzone_cykle,wydluzenie,true_wydluzenie,wytrzymalosc,true_naprezenie = np.loadtxt(nazwa_pliku,unpack=True,delimiter="\t")
#Rm, R0,2
Rm=max(naprezenie)
x02,y02,R02,a=er02(20,70)
wykres()
choice=input("Czy linia trendu wyszła poprawnie? (t/n) ")
while choice!="t":
	x=int(input("Podaj punkt początkowy dla ustalania linii trendu (np.20): "))
	y=int(input("Podaj punkt końcowy dla ustalania linii trendu (np.70): "))
	x02,y02,R02,a=er02(x,y)
	wykres()
	choice=input("Czy teraz linia trendu wyszła poprawnie? (t/n) ")
A=A(a)
#Zamiana na jednostki
E=str("{:.2f}".format(a))+" GPa"
Rm=str("{:.2f}".format(Rm))+" MPa"
R02=str("{:.2f}".format(R02))+" MPa"
A=str("{:.2f}".format(A))+" %"
print("E = "+E)
print("Rm = "+Rm)
print("R0,2 = "+R02)
print("A = "+A)