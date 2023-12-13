a=[1,2,3,4,5,6]
b=a
l=[]
for i in a:
    for j in b:
          l.append(sum([i,j]))
for i in range(2,13):
    print("probabulity of  {} is {}".format(i , l.count(i)/36))
