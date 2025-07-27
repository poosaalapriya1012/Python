arr=[1,2,1,3,5,2,4,2]
n=len(arr)
c=0
for i in range(n-2):
    if arr[i]+arr[i+2]==arr[i+1]:
        c+=1
print(c)
