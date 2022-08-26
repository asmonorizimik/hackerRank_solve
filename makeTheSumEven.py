# t=int(input())
# for _ in range(t):
#     u=int(input())
#     l=list(map(int,input().split()))
#     p=sum(l)
#     if(p%2==0):
#         print(0)
#     elif 2 in l:
#         print(1)
#     else:
#         print(-1)


t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    sum=0
    for j in range(n):
        if j in l:
            sum=sum+j
    if(sum%2==0):
        print(0)
    elif 2 in l:
        print(1)
    else:
        print(-1)