#Given an array of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). 
#It is guaranteed that Q1, Q2 and Q3 are integers.

#Input Format:
#The first line contains an integer, N, denoting the number of elements in the array. 
#The second line contains N space-separated integers describing the array's elements.

#Output:
#Print 3 lines of output in the following order:
#The first line should be the value of Q1.
#The second line should be the value of Q2.
#The third line should be the value of Q3.

#-------------------------------------SOLUTION---------------------------------------------------------------------------------------

totalnum=int(input())
num=[int(x) for x in input().split()]
sortlist=sorted(num)
lowerlst=[]
upperlst=[]
#-----------find median for any list (common function for all--------------
def median(a):
    N=len(a)
    if (N%2==0):  
        #array indexing start from zero so we need to subtract 1 from each index
        return ((a[(N//2)-1] + a[(N//2)])/2)
    else:
        return (a[((N+1)//2)-1])
    
m=median(sortlist)         #This is Q2

#----------------Create lists for Q1 and Q3-----------------------------------
# divide the list into lower and upper list 
for i in sortlist:
    if i < m:
        lowerlst.append(i)
    if i>m:
        upperlst.append(i)
    if i==m:
        pass
    
#-------------------Print Q1, Q2,Q3-----------------------------------------------
    
q1=int(median(lowerlst))
q2=int(m)
q3=int(median(upperlst))
print(q1,q2,q3, sep="\n")
        
    
    
