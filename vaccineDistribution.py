# ceil()



# for i in range(int(input())):
#     n,d=map(int,input().split())
#     age=list(map(int,input().split()))
#     l=[]
#     day=0
#     for a in age:
#         if a<=9 or a>=80:
#             l.append(a)
#     t=n-len(l)
#     if len(l)%d==0:
#         day=int(len(l)/d)
#     else:
#         day=int((len(l)/d)+1)
#     if t%d==0:
#         day+=int(t/d)
#     else:
#         day+=int((t/d)+1)
#     print(day)
    


# 2
# 10 1
# 10 20 30 40 50 60 90 80 100 1
# 5 2
# 9 80 27 72 79





# t=int(input())
# for i in range(t):
#     n,d=map(int,input().split())## no of people for a day
#     age=list(map(int,input().split()))##ages of the people
#     l=[]
#     day=0
#     for j in age:
#         if j<=9 or j>=80:
#             l.append(j)###apeople at the risk 
#     t=n-len(l)
#     if len(l)%d==0:
#         day=int(len(l)/d)
#     else:
#         day=int(len(l)/d)+1
#     if t%d==0:
#         day+=int(t/d)
#     else:
#         day+=int(t/d)+1
#     print(day)