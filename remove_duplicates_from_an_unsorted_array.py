#Remove Duplicates From an Unsorted Array
def remove_duplicates(arr):
    s=set()
    res=[]
    for i in arr:
        if i not in s:
            s.add(i)
            res.append(i)
    return res


arr = [1, 2, 3, 2, 4, 5, 1]
result = remove_duplicates(arr)
print(result)  
