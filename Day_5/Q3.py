"""you are going to write a program that calculates the sum of all the even numbers from 1 to X.
 If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100"""
target = int(input()) 
even_sum=0
for number in range(2, target+1):
  if number%2==0:
    even_sum+=number
print(even_sum)