n=5
arr=[1,4,2,9,5]
mini=float('inf')

for i in range(n):
    for j in range(i+1,n):
        avg=(arr[i]+arr[j])/2
        new=[x if x>=avg else 0 for x in arr]
        newsum=sum(new)
        mini=min(mini,newsum)
    
print(mini)