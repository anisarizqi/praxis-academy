
def SelectionSort(val):
	for isi in range(len(val)-1,0,-1):
		Max=0
		for lokasi in range(1,isi+1):
			if val[lokasi]>val[Max]:
				Max = lokasi

		temp = val[isi]
		val[isi] = val[Max]
		val[Max] = temp

ListAngka = [23,7,32,99,4,15,11,20]
SelectionSort(ListAngka)
print(ListAngka)