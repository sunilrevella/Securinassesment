from collections import defaultdict


l=[]
d=dict()

def undoom(a,b):
    l=[]
    for i in a:
        for j in b:
            l.append(sum([i,j]))
    for i in range(2,13):
                     
                     d[i]=l.count(i)
    validate(0,0)
probabulity = d

def printdd():
    
    print("Die A-->", end=" ")
    for i in range(6):
        print(A[i], end=",")
    print()
    print("Die B-->", end=" ")
    for i in range(6):
        print(B[i], end=",")
    print()

def checkcombination():
    
    calprob=defaultdict(int)
    for i in range(6):
        for j in range(6):
            calprob[A[i] + B[j]] += 1
    if(probabulity == calprob):
        return 1
    else:
        return 0

def validate(RA, RB):
    if RA == 6 and RB == 6:
        if checkcombination():
            printdd()
            print("Pairs are Finally found")
            exit(1)
        return 
    for k in range(4):
        RAF = k + 1
        for l in range(11):
            RBF = l + 1
            A[RA] = RAF
            B[RB] = RBF
            validate(RA + 1, RB + 1)
A = [0,0,0,0,0,0]
B = [0,0,0,0,0,0]
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]


undoom(a,b)

