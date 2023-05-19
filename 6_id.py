import pandas as pd
import numpy as np
import math

data=pd.read_csv("weather.csv")
features=[feat for feat in data]
features.remove('play')

class node:
    def __init__(self):
        self.child=[]
        self.value=""
        self.isLeaf=False
        self.pred=""

def entropy(example):
    p=0.0
    n=0.0
    for _, row in example.iterrows():
        if row['play']=='yes':
            p+=1
        else:
            n+=1
    if p==0.0 or n==0.0:
        return 0.0
    else:
        p=p/(p+n)
        n=n/(n+p)
        return -(p*math.log(p,2)+n*math.log(n,2))

def info_gain(example,attr):
    uniq=np.unique(example[attr])
    gain=entropy(example)
    for u in uniq:
        subdata=example[example[attr]==u]
        sub_e=entropy(subdata)
        gain-=(float(len(subdata))/float(len(example)))*sub_e
    return gain

def ID3(example,attrs):
    root=node()
    max_gain=0
    max_feat=""

    for feature in attrs:
        gain=info_gain(example,feature)
        if gain> max_gain:
            max_gain=gain
            max_feat=feature
    root.value=max_feat

    uniq=np.unique(example[max_feat])
    for u in uniq:
        subdata=example[[example[max_feat]==u]]
        sub_e=entropy(subdata)
        if sub_e ==0.0:
            newNode=node()
            newNode.value=u
            newNode.isLeaf=True
            newNode.pred=np.unique(subdata['play'])
            root.child.append(newNode)
        else:
            dummyNode=node()
            dummyNode.value=u
            new_attrs=attrs.copy()
            new_attrs.remove(max_feat)
            child=ID3(subdata,new_attrs)
            dummyNode.child.append(child)
            root.child.append(dummyNode)
    return root


def PrintTree(root:node,depth=0):
    print("h")
    for i in range(depth):
        print("\t",end="")
    print(root.value,end="")
    if root.isLeaf:
        print("->",root.pred)
    print()
    for child in root.children:
        printTree(child,depth+1)

def classify(root: node,new):
    for child in root.children:
        if child.value==new[root.value]:
            if child.isLeaf:
                print("Predicted label for new example:", new," is: ",child.pred)
                exit
            else:
                classify(child.children[0],new)

root=ID3(data,features)
print("Decision Tree")
PrintTree(root)
    

    
    
            
            
        
    

    
    
    


