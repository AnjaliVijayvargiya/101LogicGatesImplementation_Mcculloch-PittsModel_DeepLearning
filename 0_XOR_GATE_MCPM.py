# importing Python library 
import numpy as np 

# design McCulloch And Pitts Model 
def MCPModel(x, w): 
	v = np.dot(w, x)
	y = XORThreshold(v) 
	return y

# define Unit Step Function 
def XORThreshold(v): 
	if v == 1: 
		return 1
	else: 
		return 0

# AND Logic Function 
# w1 = 1, w2 = 1  both are same, no learning is here, just adjusting the threshold to get correct results.
#we can add bias for adjusting and fix the threshold in that case
def XORGate(x): 
	w = np.array([1, 1])
	return MCPModel(x, w) 

# testing the McCulloch And Pitts Model 
test1 = np.array([0, 0])
test2 = np.array([0, 1]) 
test3 = np.array([1, 0])
test4 = np.array([1, 1])

print("XOR({}, {}) = {}".format(0, 0, XORGate(test1))) 
print("XOR({}, {}) = {}".format(0, 1, XORGate(test2))) 
print("XOR({}, {}) = {}".format(1, 0, XORGate(test3))) 
print("XOR({}, {}) = {}".format(1, 1, XORGate(test4))) 
