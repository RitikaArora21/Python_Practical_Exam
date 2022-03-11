#sum of first n odd numbers
def oddSum(n) :
    sum = 0
    first = 1
    p = 0
    while p < n:
        sum = sum + first
        first = first + 2
        p = p + 1
    return sum
n=6

print (" Sum of first" , n, "odd numbers is: ",oddSum(n))

#sum of first n even numbers
def evensum(n):
    first = 2
    sum = 0
    i = 1
     
    # sum of first n even numbers
    while i <= n:
        sum += first
         
        # next even number
        first += 2
        i = i + 1
    return sum

n = 3
print("sum of first ", n, "even number is: ",
      evensum(n))
      
#sum of n natural numbers
num = 10


if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum of n numbers is", sum)
