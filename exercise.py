a=list(map(int,input().split()))
i=0
even=[]
odd=[]
while i<len(a):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
    i+=1
even.extend(odd)
print(even)
j=0
while j<len(even):
    print(even[j],end=' ')
    j+=1

