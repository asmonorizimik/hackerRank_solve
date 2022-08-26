
# T=int(input())
# for i in range(T):
#     A,B=map(int,input().split())
#     A_even=A//2
#     B_even=B//2
#     A_odd=A_even+A%2
#     B_odd=B_even+B%2
#     res=(A_even*B_even)+(A_odd*B_odd)
#     print(res)


t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    a_even=a//2
    a_odd=a-a_even
    b_even=b//2
    b_odd=b-b_even
    result=(a_even*b_even)+(a_odd*b_odd)
    print(result)
