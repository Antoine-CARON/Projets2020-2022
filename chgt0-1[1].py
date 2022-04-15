list=[1,1,0,1,1,0,1,1,0,0,0]
def chgt(listbase,x):
	liste=listbase
	if x<len(list):
		chgt(liste,x+1)
		if liste[x]==0:
			liste[x]=1
			x=x+1
		elif liste [x]==1:
			liste[x]=0
			x=x+1
		return liste
print(chgt(list,0))