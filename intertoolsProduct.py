A=list(map(int,input().split()))
B=list(map(int,input().split()))
i=0
while i<len(A):
    j=0
    while j<len(B):
        print((A[i],B[j]),end=' ')
        j+=1
    i+=1

# Sample Input

#  1 2
#  3 4
# Sample Output

#  (1, 3) (1, 4) (2, 3) (2, 4)