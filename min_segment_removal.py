def min_remove_length(n, s):
    s=list(s)
    for i in range(n):
        if s[i]=='I':
            s[i]='F'
            break
    s=''.join(s)
    if 'I' not in s:
        return 0
    f=s.find('I')
    l=s.rfind('I')
    
    return l-f+1


n = 10
s = "FIFFIIFFFI"
print(min_remove_length(n, s))  # Output: 6
