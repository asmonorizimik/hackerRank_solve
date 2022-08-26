# s=input()
# prev_c=''
# count=0
# Out=()
# for c in s :
#     if c == prev_c:
#         count+=1
#     else:
#         if prev_c!='':
#             print((count+1,int(prev_c)), end=" ")
#         prev_c=c
#         count=0
# print((count+1,int(prev_c)),end=" ")



# Sample Input
# 1222311
# Sample Output
# (1, 1) (3, 2) (1, 3) (2, 1)
# Explanation
# First, the character 1 occurs only once. It is replaced by (1,1). 
# Then the character 2 occurs three times, and it is replaced by (3,2) and so on.
# Also, note the single space within each compression and between the compressions.





string=input()
s=""
c=0
i=0
while i<len(string):
    if string[i]==s:
        c+=1
    else:
        if s!='':
            print((c+1,int(s)),end='')
        s=string[i]
        c=0
    i+=1
print((c+1,int(s)),end='')