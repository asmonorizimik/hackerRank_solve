def countingValleys(steps, path):
    # Write your code here
    # valleys = 0
    # cur_level = 0
    # for steps in path:
    #     if(steps == 'U'):
    #         cur_level += 1
    #         if(cur_level == 0):
    #             valleys += 1
    #     elif(steps == 'D'):
    #         cur_level -= 1
    # return(valleys)



    # Write your code here
    valley=0
    level=0
    i=0
    while i<len(path):
        if path[i]=="U":
            level+=1
            if level==0:
                valley+=1
        elif path[i]=="D":
            level-=1
        i+=1
    return valley
                
steps = int(input().strip())

path = input()
print(countingValleys(steps,path))


# The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.
# Sample Input

# 8
# UDDDUDUU
# Sample Output

# 1