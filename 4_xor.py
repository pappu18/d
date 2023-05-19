import numpy as np

def unitStep(v):
    if v>=0: return 1
    else: return 0

def percep(x,w,b):
    v=np.dot(x,w)+b
    y=unitStep(v)
    return y

def AND(x):
    w=np.array([1,1])
    b=-1.5
    return percep(x,w,b)

def NOT(x):
    w_not=-1
    b_not=0.5
    return percep(x,w_not,b_not)

def OR(x):
    w_or=np.array([1,1])
    b_or=-0.5
    return percep(x,w_or,b_or)

def XOR(x):
    y1=AND(x)
    y2=OR(x)
    y3=NOT(y1)
    final=np.array([y2,y3])
    output=AND(final)
    return output

t1=np.array([0,0])
t2=np.array([0,1])
t3=np.array([1,0])
t4=np.array([1,1])

print(XOR(t1))
print(XOR(t2))
print(XOR(t3))
print(XOR(t4))
