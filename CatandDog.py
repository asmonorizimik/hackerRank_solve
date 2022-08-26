T=int(input())
for _ in range(T):
    Cat,Dog,Legs=map(int,input().split())
    total = (Cat+Dog)*4
    min_no=Cat-Dog*2
    if(total>=Legs and Legs%4==0 and (Dog+min_no)*4<=Legs):
        print("yes")
    else:
        print("no")
