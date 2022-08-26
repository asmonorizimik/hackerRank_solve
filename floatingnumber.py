c=int(input().strip())
for i in range(c):
    result=False
    try:
        string=input().strip()
        number=float(string)
        result=True
        number=int(string)
        result=False
    except:
        pass
    print(result)