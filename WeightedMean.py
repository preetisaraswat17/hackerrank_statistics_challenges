n=int(input())
num=[int(x) for x in input().split(" ")]
weight=[int(x) for x in input().split(" ")]

#first is a nested list with [num,weight] sub lists pairs
final = zip(num, weight)

# now we create a new list m that maps every element of final to num*weight[10, 80, 90, 200,100]
m=list(map(lambda x: (x[0]*x[1]), final))

#finally calculate mean using sum of m /sum of weights
mean=lambda x,y: sum(x)/sum(y) 
#round it to 1 digit decimal
print(round(mean(m,weight),1))
