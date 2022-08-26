# Total amount of food required for all 
# rats = r * unit = 7 * 2 = 14. 
# The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food in 1st 4 houses is sufficient for all the rats.
#  Thus, output is 4.



# numberOfRats=int(input())
# unit=int(input())##amount of food each rat consume
# sizeOfArray=int(input())
# array=list(map(int,input().split()))
# print(array)
# if sizeOfArray==0:
#     print(-1)
# totalFoodRequire=numberOfRats*unit
# i=0
# amountOffood=0
# while i<=sizeOfArray:
#     amountOffood+=array[i]
#     i+=1
#     print(amountOffood)
#     if amountOffood>=totalFoodRequire:
#         print(i)
#         break
#     else:
#         print(0)




# def calculate(r,unit,arr,n):
#     if n==0:
#         return -1
#     totalFoodRequired=r*unit
#     amountOfFood=0
#     for j in range(n):
#         amountOfFood+=arr[j]
#         if amountOfFood >= totalFoodRequired:
#             break
#     if totalFoodRequired > amountOfFood:
#         return 0
#     return j
# r = int(input())
# unit = int(input())
# n = int(input())
# arr = list(map(int,input().split()))
# print(calculate(r,unit,arr,n))






def RatCount(rats,unit,sizeOfarray,array):
    if sizeOfarray==0:
        return -1
    requiredFood=rats*unit##amount of food that each rat consume
    amountOfFood=0
    i=0  ## number of house
    while i<=sizeOfarray:
        amountOfFood+=array[i]
        if amountOfFood >= requiredFood:
            break
        i+=1
    if amountOfFood >= requiredFood:
        return i+1
    else:
        return 0
rats=int(input())
unit=int(input())
sizeOfarray=int(input())
array=list(map(int,input().split()))
print(RatCount(rats,unit,sizeOfarray,array))