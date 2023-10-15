''' 


''' 
import numpy as np 

#UNCOMMENT THE BELOW THREE LINES TO TEST FOR SAMPLE DATA
#nazidims = np.array([3,2]) # mediocre
#crossdims =  np.array([4,4]) # max dims
#Hdims =  np.array([1,2]) # min dims  

def paracompare(shape,paralist):
	check = 0
	for i in range(len(paralist)):
		if shape[i] < paralist[i]:
			check += 1
	print("check=",check)
	if check == 2:
		return 1 #yes
	else: 
		return 0 #no

def morph(d1,d2): 
	dimlist = np.array([d1,d2])
	if paracompare(crossdims,dimlist) == 1:
	    #cross()
	    print("CROSS shape")
	elif paracompare(nazidims,dimlist) == 1:
		#nazi()  
		print("NAZI shape")
	elif paracompare(Hdims,dimlist) == 1: 
		#H()
		print("H shape")

	else:
		print("""
ERROR: cannot determine shape
either debug, change drone-size or move on
		""") 

#UNCOMMENT THIS LINE TO TEST WITH SAMPLE DATA
#morph(5,5,6)
