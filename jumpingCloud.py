def jumpingOnClouds(c):
    i = 0
    jumpCount = -1
    while i < len(c):
        jumpCount += 1
        if (i < len(c)-2) and (c[i+2] == 0):
            i+=1
        i += 1
    return jumpCount
n = int(input())
c = list(map(int, input().rstrip().split()))
print(jumpingOnClouds(c))
