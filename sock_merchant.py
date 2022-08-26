# def sockMerchant(n, ar):
#     num1 = 0
#     for i in range(0,n):
#         num2 = 1
#         for j in range(i+1,n):
#             if ar[i] == None:
#                 continue
#             if ar[i] == ar[j] and num2 ==1:
#                 num1 = num1 + 1
#                 num2 = num2 + 1
#                 ar[j] = None
            
#     return num1
# n=int(input())
# ar=list(map(int,input().split()))
# print(sockMerchant(n,ar))










# def sockMerchant(n, ar):
#     ar.sort()
#     result=0
#     i=0
#     j=1
#     while i<n:
#         if n==1:
#             return 0
#         if ar[i]==ar[j]:
#             result+=1
#         i+=1
#         j+=1
#         i+=1
#         j+=1
#         if j==len(ar):
#             break
#     return result





# from collections import Counter
# n=input()
# socks, pairs = Counter(map(int,input().strip().split())), 0
# for s in socks:
#     pairs += socks[s]//2
# print(pairs)




# from collections import Counter
# def sockMerchant(n,socks):
#     pair=0
#     for i in socks:
#         pair+=socks[i]//2
#     return pair
# n=int(input())
# socks=Counter(map(int,input().strip().split()))
# print(sockMerchant(n,socks))



def sockMerchant(n, ar):
    num1 = 0
    i=0
    while i<len(ar):
        num2 = 1
        for j in range(i+1,n):
            if ar[i] == None:
                continue
            if ar[i] == ar[j] and num2 ==1:
                num1 = num1 + 1
                num2 = num2 + 1
                ar[j] = None
        i+=1
    return num1
n=int(input())
ar=list(map(int,input().split()))
print(sockMerchant(n,ar))
