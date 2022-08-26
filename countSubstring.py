# Sample Input
# ABCDCDC
# CDC
# Sample Output
# 2
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the 
# given string. String traversal will take place from left to right, not from right to left



def count_substring(string,sub_string):
    i=0
    while i<len(string):
        
        count=0
    return count    
string=input()
sub_string=input()
print(count_substring(string,sub_string))






##The startswith() method returns True if the string starts with the specified value, otherwise False. Syntax. string.

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count
# string=input()
# sub_string=input()
# print(count_substring(string,sub_string))