N=int(input("Enter the number of negative values:"))
n=[[int(j) for j in input().split()] for i in range(N)]
P=int(input("Enter the number of positive values:"))
p=[[int(j) for j in input().split()] for j in range(P)]

print("Enter the weight vector:")
w=[int(j) for j in input().split()]

count=len(w)
prev=[]

while (prev!=w):
    prev=w.copy()
    for i in n:
        temp=0
        for j in range(count):
            temp+=i[j]*w[j]
        if temp>=0:
            for k in range(count):
                w[k]-=i[k]
    for i in p:
        temp=0
        for j in range(count):
            temp+=i[j]*w[j]
        if temp<0:
            for k in range(count):
                w[k]+=i[k]
print("Final weight:",w)
