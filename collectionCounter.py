from collections import Counter
X = int(input()) ## number of shoes
sizes = Counter(map(int,input().split()))##size of the shoes
print(sizes)
# Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})
N = int(input()) ## no of shoes desired by the costomers
earnings = 0

for i in range(N):
    size,x = map(int,input().split()) ## size and their prize
    print(sizes[size])
    if sizes[size]>0:
        sizes[size]-=1
        earnings += x
        # print(earnings)
print (earnings)
    


# Sample Input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output
# 200


# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned =  55+40+45+60=200

# collector():A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
# Counter is a container included in the collections module\


# from collections import Counter
 
# # With sequence of items
# print(Counter(['B','B','A','B','C','A','B','B','A','C']))
 
# # with dictionary
# print(Counter({'A':3, 'B':5, 'C':2}))
 
# # with keyword arguments
# print(Counter(A=3, B=5, C=2))


# The collection Module in Python provides different types of containers.
#  A Container is an object that is used to store different objects and 
#  provide a way to access the contained objects and iterate over them