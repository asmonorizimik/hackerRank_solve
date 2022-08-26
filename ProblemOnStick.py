for _ in range(int(input())):
    n=int(input())
    # print(n)
    l=list(map(int,input().split()))
    temp=0
    l.sort()
    # print(l)
    count=0
    for i in range(n):
        if l[i]!=0 and l[i]!=temp:
            count+=1
            temp=l[i]
        # print(temp,"temp")
    print(count)


# Output
# For each test case, print a single line containing one integer ― the minimum number of operations needed to completely cut all the sticks.


#input
# 1
# 3
# 1 2 3
# output=>3