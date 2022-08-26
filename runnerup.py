# n = int(input())
# arr = map(int, input().split())
# x=list(arr)
# i=0
# l=0
# runner_up=0
# while i<len(x):
#     if x[i]>l:
#         l=x[i]
#     elif x[i]<l and runner_up<l:
#         runner_up=x[i]
#     i+=1
# print(runner_up)
        


n = int(input())
arr = map(int, input().split())
largest = 0
secondlargest = 0
for i in arr:
    if i > largest:
        tmp = largest
        largest = i
        secondlargest = tmp
    elif i > secondlargest and i != largest:
        secondlargest = i
print(secondlargest)



# n = int(input())
# arr = map(int, input().split())
# print (sorted(set(arr))[-2])




