# importing Python library 
import numpy as np 

# design McCulloch And Pitts Model 
def MCPModel(x, w): 
	v = np.dot(w, x)
	y = NOTThreshold(v) 
	return y

# define Unit Step Function 
def NOTThreshold(v): 
	if v == 0: 
		return 1
	else: 
		return 0

# AND Logic Function 
# w1 = 1, w2 = 1  both are same, no learning is here, just adjusting the threshold to get correct results.
#we can add bias for adjusting and fix the threshold in that case
def NOTGate(x): 
	w = np.array([1])
	return MCPModel(x, w) 

# testing the McCulloch And Pitts Model 
test1 = np.array([0])
test2 = np.array([1])

print("NOT({}) = {}".format(0, NOTGate(test1))) 
print("NOT({}) = {}".format(1, NOTGate(test2))) 
