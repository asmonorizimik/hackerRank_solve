# HACK 2
# Sample Output

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

from itertools import permutations


s,n1=map(str,input().split())
n=int(n1)
s1=[]
i=0
while i<len(s):
    s1.append(s[i])
    i+=1
s1.sort()
j=0
while j<len(s1):
    k=0
    while k<len(s1):
        print(s1[j]+s1[k])
        k+=1
    j+=1





# from itertools import permutations  ### intertool(package)

# s,k = input().split()

# words = list(permutations(s,int(k)))
# words = sorted(words, reverse=False)
# for word in words:
#     print(*word,sep='')
####Python provides direct methods to find permutations and combinations of a sequence. These methods are present in itertools package.
# ##permutations method:  This method takes a list as an input and returns an object list 
# of tuples that contain all permutations in a list form. 