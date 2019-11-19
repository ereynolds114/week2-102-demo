#Evan Reynolds
#CSCI 102-A
#Week 12

tot=0
num=7
fail=True
while tot<100:
    for i in range(2,num//2):
        if num%i==0:
            num+=1
            fail=True
            break
    if not fail:
        print(num)
        num+=1
