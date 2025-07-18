def fun(s, t):
    if len(s) != len(t):
            return False
    
    def transform(s):
        
        h={}
        res=[]
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=i
            res.append(h[s[i]])
            
        return res
    return transform(s)==transform(t)

print(fun("egg","add"))
