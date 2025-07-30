n=6
m=4
def calcGCD(n:int, m: int) -> int:
    
    while m!=0:
        n,m=m,n%m
    return n
print(calcGCD(n,m))
