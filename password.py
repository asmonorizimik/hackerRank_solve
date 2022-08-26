# def CheckPassword(s,n):
#     if n<4:
#         return 0
#     if s[0].isdigit():
#         return 0
#     cap=0
#     nu=0
#     for i in range(n):
#         if s[i]==' ' or s[i]=='/':
#             return 0
#         if s[i]>='A' and s[i]<='Z':
#             cap+=1
#         elif s[i].isdigit():
#             nu+=1
 
#     if cap>0 and nu>0:
#         return 1
#     else:
#         return 0
 
# s=input()
# a=len(s)
# print(CheckPassword(s,a))






def password(string,n):
    if n<4:
        return 0
    else:
        if string[0].isdigit():
            return 0
        u=0
        d=0
        for i in range(n):
            if string[i] ==" " or string[i]=="/":
                return 0
            if string[i].isupper():
                u+=1
            elif string[i].isdigit():
                d+=1
        if u>0 and d>0:
            return 1
        else:
            return 0
string=input()
n=len(string)
print(password(string,n))
        
    