# importing Python library 
import numpy as np 

# design McCulloch And Pitts Model 
def MCPModel(x, w): 
	v = np.dot(w, x)
	y = XNORThreshold(v) 
	return y

# define Unit Step Function 
def XNORThreshold(v): 
	if v == 1: 
		return 0
	else: 
		return 1

# AND Logic Function 
# w1 = 1, w2 = 1  both are same, no learning is here, just adjusting the threshold to get correct results.
#we can add bias for adjusting and fix the threshold in that case
def XNORGate(x): 
	w = np.array([1, 1])
	return MCPModel(x, w) 

# testing the McCulloch And Pitts Model 
test1 = np.array([0, 0])
test2 = np.array([0, 1]) 
test3 = np.array([1, 0])
test4 = np.array([1, 1])

print("XNOR({}, {}) = {}".format(0, 0, XNORGate(test1))) 
print("XNOR({}, {}) = {}".format(0, 1, XNORGate(test2))) 
print("XNOR({}, {}) = {}".format(1, 0, XNORGate(test3))) 
print("XNOR({}, {}) = {}".format(1, 1, XNORGate(test4))) 
