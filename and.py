import numpy as np
def unitStep(v):
    if v>=0:
        return 1
    else:
        return 0
    
def perceptronModel(x,w,b):
    v=np.dot(w,x)+b
    y=unitStep(v)
    return y

def AND(x):
    w=np.array([1,1])
    b=-1.5
    return perceptronModel(x,w,b)

def NOT(x):
    w_not=-1
    b_not=0.5
    return perceptronModel(x,w_not,b_not)

def OR(x):
    w_or=np.array([1,1])
    b_or=-0.5
    return perceptronModel(x,w_or,b_or)

def XOR(x):
    y1=AND(x)
    y2=OR(x)
    y3=NOT(y1)
    final=np.array([y2,y3])
    output=AND(final)
    return output

test1=np.array([0,0])
test2=np.array([0,1])
test3=np.array([1,0])
test4=np.array([1,1])

print("AND ({}, {}) = {}".format(0,0,AND(test1)))
print("AND ({}, {}) = {}".format(0,1,AND(test2)))
print("AND ({}, {}) = {}".format(1,0,AND(test3)))
print("AND ({}, {}) = {}".format(1,1,AND(test4)))
'''print("XOR ({}, {}) = {}".format(0,0,XOR(test1)))
print("XOR ({}, {}) = {}".format(0,1,XOR(test2)))
print("XOR ({}, {}) = {}".format(1,0,XOR(test3)))
print("XOR ({}, {}) = {}".format(1,1,XOR(test4)))'''
