# t=int(input())
# for i in range(t):
#     n,k,x,y = map(int,input().split())
#     j=x
#     while  x <=n:
#         if x==y:
#             print("YES")
#             break
#         x=(x+k)%n
#         if x==j:
#             print("NO")
#             break
# N="no. of citiies"
# k="the size of jumps"
# x="covid's current city"
# y="city that i live"
#j=current city






# test_case=int(input())
# for i in range(test_case):
#     N,K,X,Y = map(int,input().split())
#     a=[]
#     while True:
#         if (X+K)%N not in a:
#             a.append((X+K)%N )
#             X=(X+K)%N
#             if X==Y:
#                 print("YES")
#                 break
#         else:
#             print("NO")
#             break
    


####covid run jumping city by city

for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    a=[]
    while x<n:
        if x in a:
            print("NO")
            break
        elif(x==y):
            print("YES")
            break
        a.append(x)
        x=(x+k)%n
# N="no. of citiies"
# k="the size of jumps"
# x="covid's current city"
# y="city that i live"
#a=list of covid's current city
        