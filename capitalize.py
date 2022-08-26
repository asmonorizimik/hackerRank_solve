# def solve(s):
#     x=s.split()
#     print(x)
#     a=''
#     for i in x:
#         a=a+i.capitalize()+' '
#     return a
# s="welcome to my home"
# a=solve(s)
# print(a)



### story: Return every first letter with uppercase eg: "my name Is Manori" =>My Name Is Manori

# def solve(s):
#     x=s.split()
#     print(x)
#     s=''
#     i=0
#     while i<len(x):
#         a=''
#         j=0
#         while j<len(x[i]):
#             y=x[i][0].upper()
#             if j>0:
#                 a+=x[i][j]
#             b=y+a+' '
#             j+=1
#         s+=b
#         n=s[:-1]
#         i+=1
#     return n
# print(solve(input()))



   