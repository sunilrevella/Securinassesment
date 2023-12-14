
from collections import defaultdict

A = [0,0,0,0,0,0]
B = [0,0,0,0,0,0]
probabulity = {2: 1,3: 2,4: 3,5: 4,6: 5,7: 6,8: 5,9: 4,10: 3,11: 2,12: 1}
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
    printdd()
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

validate(0,0)

