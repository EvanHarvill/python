#basecon.py kriptic

def bincon(num,addSpace):
	n = num
	s = addSpace
	#print(n,s)
	print(n," = ",end="")
	d = 128
	binString ="" #create a string called binString
	for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		#print(d,q,r)# debug line
		n = r
		d = int(d / 2)
		binString = binString+str(q)
	#print(binString)
	
def main():
	bincon(191,0)
	bincon(7,0)
	bincon(15,0)
	bincon(31,0)
main()
