import random
c1=0
c2=0
while True:
    print("enter your choice \n press 1 for rock \n 2for paper \n 3 for scissors")
    a=int(input("user turn:"))
    b=random.randrange(1,3)
    print("computer choose ",b)
    if a==b:
        print("tie")
        c1=c1+1
        c2=c2+1
    elif a==1:
        if b==2:
            print("you lose")
            c1=c1+1
        else:
            print("you won")
            c1=c1+1
    elif a==2:
        if b==1:
            print("you won")
            c2=c2+1
        else:
            print("you lose")
            c1=c1+1
    else:
        if b==1:
            print("you lose")
            c1=c1+1
        else:
            print("you won")
            c2=c2+1
    print("do u want to play more??\n if no press n else press any key")
    u=input()
    if u =='n' or u=='N':
        break
print("thank u for playing")
print("your score is %d and computer score is %d"%(c2,c1))


    

