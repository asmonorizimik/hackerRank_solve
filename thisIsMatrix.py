# Sample Input 0
# 7 3
# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!
# Sample Output 0
# This is Matrix#  %!

# ['Tsi','h%x','i #','sM ','$a ','#t%','ir!']


first_multiple_input = input().split()
print(first_multiple_input)
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_items = input()
    matrix_item=matrix_items[:m]
    matrix.append(matrix_item)

i=0
while i<len(matrix):
    j=0
    s=""
    while j<len(matrix[i]):
        x=matrix[i][j]+matrix[j][i]
        s+=x
        j+=1
        print(s,end=' ')
    i+=1



