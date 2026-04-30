# Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.
num=list(range(1,51))
for n in num:
 if n%5==0 and n%7==0:
  print(n)
val=range(10,41)
total=sum(val)
val=len(val)
average=total/val
print(average)
odd=list(range(10,51))
for o in odd[:20]:
 if o%2!=0:
  print(o)
num=int(input('Enter number: '))
for m in range(1,11):
  print(num,'x',m,'=',num*m)
even_numbers=list(range(1,51))
for k in even_numbers:
 if k%2==0:
  print(k)
ls1 = [ ('Jay', '20'), ('Mo', '30'), ('Mya', '32') ]
for k in ls1:
 print(k)