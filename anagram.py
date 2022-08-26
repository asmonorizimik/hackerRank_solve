# def construct(ransom_note, magazine):
#     d = {}
#     for letter in magazine:
#         if letter in d:
#             d[letter] += 1
#         else:
#             d[letter] = 1
#     for char in ransom_note:
#         if char not in d and d[char]== 0:
#             return False
#         d[char] -= 1
#     return True
# print(construct(input("enter note"),input("enter megazine")))




# def anagram(first_string, sec_string):
#     d = {}
#     for letter in sec_string:
#         if letter in d:
#             d[letter] += 1
#         else:
#             d[letter] = 1
#     for char in first_string:
#         if char not in d and d[char]== 0:
#             return "false"
#         d[char] -= 1
#     return "yes"
# first_string=input() 
# sec_string=input()
# print(anagram(first_string, sec_string))



 




# def angram(str1,str2):
#     if(len(str1) == len(str2)):
#         sorted_str1 = sorted(str1)
#         sorted_str2 = sorted(str2)
#         if(sorted_str1 == sorted_str2):
#             print("yes")
#         else:
#             print("no")
#     else:
#         pass
# str1,str2=map(str,input().split())
# angram(str1,str2)


###construct the word==>eg: silent and lisent will return 1 else 0

# def check(s1, s2):
#     if(sorted(s1)== sorted(s2)):
#         return 1
#     else:
#         return 0        
# s1 =input()
# s2 = input()
# print(check(s1, s2))

