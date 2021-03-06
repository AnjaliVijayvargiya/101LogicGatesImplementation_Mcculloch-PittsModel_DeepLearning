# importing Python library 
import numpy as np 

# design McCulloch And Pitts Model 
def MCPModel(x, w): 
	v = np.dot(w, x)
	y = ANDThreshold(v) 
	return y

# define Unit Step Function 
def ANDThreshold(v): 
	if v > 1: 
		return 1
	else: 
		return 0

# AND Logic Function 
# w1 = 1, w2 = 1  both are same, no learning is here, just adjusting the threshold to get correct results.
#we can add bias for adjusting and fix the threshold in that case
def ANDGate(x): 
	w = np.array([1, 1])
	return MCPModel(x, w) 

# testing the McCulloch And Pitts Model 
test1 = np.array([0, 0])
test2 = np.array([0, 1]) 
test3 = np.array([1, 0])
test4 = np.array([1, 1])

print("AND({}, {}) = {}".format(0, 0, ANDGate(test1))) 
print("AND({}, {}) = {}".format(0, 1, ANDGate(test2))) 
print("AND({}, {}) = {}".format(1, 0, ANDGate(test3))) 
print("AND({}, {}) = {}".format(1, 1, ANDGate(test4))) 
