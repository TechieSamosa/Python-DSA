#we will be writing code to find the sum of n natural numbers in python
#using formula
n = int(input("Enter the number till which you want the sum ==>"))
sum_for = ((n/2)*(2+(n-1)))
print (sum_for)

#now using loop and a variable called sum
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)
