# Sample Input

# HACK 2
# Sample Output

# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK


# from itertools import combinations

# io = input().split()
# S = io[0]
# k = int(io[1])
# for i in range(1,k+1):
#     for j in combinations(sorted(S),i):
#         print("".join(j))
# print(io)



from itertools import combinations
s,n=input().split()
for i in range(1,int(n)+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))
print(s,n)
