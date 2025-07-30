n=6
m=4
def calcGCD(n:int, m: int) -> int:
    
    def factors(num):
        res=[]
        for i in range(1,num+1):
            if num%i==0:
                res.append(i)
        return res
    nf=factors(n)
    mf=factors(m)
    new=set(nf) & set(mf)
    return max(new)
print(calcGCD(n,m))
