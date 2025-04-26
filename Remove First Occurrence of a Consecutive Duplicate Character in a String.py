s="422323"
hash=set()
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        res=s.replace(s[i],'',1)
        break
    else:
        pass

print(res)
        