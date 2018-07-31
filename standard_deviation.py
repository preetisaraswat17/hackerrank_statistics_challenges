#Given an array, n, of  integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 
#decimal place . An error margin of  will be tolerated for the standard deviation.

#Input Format
#The first line contains an integer,n , denoting the number of elements in the array. 
#The second line contains n space-separated integers describing the respective elements of the array.

#Output Format
#Print the standard deviation on a new line


#--------------------------------------Solution-------------------------------------------------------------------------------------

from math import sqrt

n=int(input())
num=[int(x) for x in input().split()]
#---------------step1-Calculate Mean----------------------
mean=sum(num)/n

#---------------step2-calculate squared diff---------------
sqdiff=list(map(lambda i:(i-mean)**2, num))
variance=sum(sqdiff)/n

#------------------step3-Calculate standard deviation-------
std=sqrt(variance)
print(std)
