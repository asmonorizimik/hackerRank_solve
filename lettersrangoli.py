# size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----





# def print_rangoli(size):
#     width  = size*4-3
#     string = ''

#     for i in range(1,size+1):
#         for j in range(0,i):
#             string += chr(96+size-j)
#             if len(string) < width :
#                 string += '-'
#         for k in range(i-1,0,-1):    
#             string += chr(97+size-k)
#             if len(string) < width :
#                 string += '-'
#         print(string.center(width,'-'))
#         string = ''

#     for i in range(size-1,0,-1):
#         string = ''
#         for j in range(0,i):
#             string += chr(96+size-j)
#             if len(string) < width :
#                 string += '-'
#         for k in range(i-1,0,-1):
#             string += chr(97+size-k)
#             if len(string) < width :
#                 string += '-'
#         print(string.center(width,'-'))
# print_rangoli(int(input()))



