# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0

# 56.00




n = int(input())
student_marks = {}
for i in range(n):
    name, *i = input().split()
    scores = list(map(float, i))
    student_marks[name] = scores

query_name = input()
p=student_marks[query_name]
sum=0
for j in p:
    sum+=j
per=(sum/len(p)*100)/100
print('%.2f' % per)