list=["zero","one","two","three"]
list1=["numbers","snacks"]
list2=["choco","chips","biscuit","bhel"]
l=[]
d={}
d1={}
d2={}
i=0
while i<len(list):
    d1[i]=list[i]
    d2[i+1]=list2[i]
    i+=1
    l.append(d1)
    l.append(d2)
j=0
while j<len(list1):
    d[list1[j]]=l[j]
    j+=1
print(d)