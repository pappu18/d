N=int(input('Enter the number of negative values:'))
n=[[int(i) for i in input().split()]for j in range(N)]
P=int(input('Enter the number of positive values:'))
p=[[int(i) for i in input().split()] for j in range(P)]

print("Enter the weight vector:")
w=[int(i) for i in input().split()]

prev=[]
count=len(w)
while prev!=w:
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
        for l in range(count):
            temp+=w[l]*i[l]
        if temp<0:
            for m in range(count):
                w[m]+=i[m]

print("The final weight vector: ",w)

