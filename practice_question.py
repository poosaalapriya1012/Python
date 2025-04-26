L=10
R=11
n=22
sum1=0
res=""
for i in range(L,R+1):
    sum1+=i
if sum1==n:
    res="neutral"
if sum1<n:
    diff=n-sum1
    res="add "+ str(diff)
if sum1>n:
    diff=sum1-n
    res="decrease "+ str(diff)
print(res)
        