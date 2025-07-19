n=36
k=6 
res=[]

for i in range(1,n+1):
    if n%i==0:
        res.append(i)
l=len(res)
print(res)
print(res[-k])
        