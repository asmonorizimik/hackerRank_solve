def swapcase(s):
    s1=''
    i=0
    while i<len(s):
        if s[i].islower():
            a=s[i].upper()
            s1+=a
        else:
            a1=s[i].lower()
            s1+=a1
        i+=1
    return s1
s= 'HackerRank.com presents "Pythonist 2".'
print(swapcase(s))