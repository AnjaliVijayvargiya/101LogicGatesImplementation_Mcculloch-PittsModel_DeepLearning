# importing Python library 
import numpy as np 

# design McCulloch And Pitts Model 
def MCPModel(x, w): 
	v = np.dot(w, x)
	y = NANDThreshold(v) 
	return y

# define Unit Step Function 
def NANDThreshold(v): 
	if v > 1: 
		return 0
	else: 
		return 1

# AND Logic Function 
# w1 = 1, w2 = 1  both are same, no learning is here, just adjusting the threshold to get correct results.
#we can add bias for adjusting and fix the threshold in that case
def NANDGate(x): 
	w = np.array([1, 1])
	return MCPModel(x, w) 

# testing the McCulloch And Pitts Model 
test1 = np.array([0, 0])
test2 = np.array([0, 1]) 
test3 = np.array([1, 0])
test4 = np.array([1, 1])

print("NAND({}, {}) = {}".format(0, 0, NANDGate(test1))) 
print("NAND({}, {}) = {}".format(0, 1, NANDGate(test2))) 
print("NAND({}, {}) = {}".format(1, 0, NANDGate(test3))) 
print("NAND({}, {}) = {}".format(1, 1, NANDGate(test4))) 
