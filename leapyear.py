# year=int(input("enter the year:"))
# if year%100==0:
#     if year%400==0:
#         print(year,"is a leap year")
#     else:
#         print("century year")
# else:
#     if year%4==0:
#         print(year,"is a leap year")
#     else:
#         print("not leap year nor century year")






def is_leap(year):
    leap = False
    if (year % 100 == 0) and (year %400 != 0):
        leap = False
    elif (year % 4 == 0):
        leap = True
    return leap
year=int(input())
print(is_leap(year))



# def is_leap(year):
#     leap = False
#     if year%400!=0 and year%100==0:
#         leap=False
#     else:
#         if year%4==0:
#             leap=True
#     return leap

# year = int(input())
# print(is_leap(year))









