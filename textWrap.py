# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

s="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
num=int(input("enter the number: "))
# i=0
# a=""
# while i<len(s):
#     a+=s[i:i+num]+"\n"
#     i+=num
# print(a)




def wrap(string, max_width):
    s = ""
    for c in range(0,len(string),max_width):
        s += string[c:c+max_width] + "\n"
    return s
print(wrap(s,num))


    