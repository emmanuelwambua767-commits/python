teams=('Liverpool','Manchester United','Manchester City')
for z in teams:
    print(z)
numbers=list(range(10,101))
even_numbers=[]
for y in numbers:
   if y%2==0:
      even_numbers.append(y)
      print(even_numbers)
numbers=list(range(10,101))
uneven_numbers=[]
for x in numbers:
 if x%3==0 and x%7==0:
    uneven_numbers.append(x)
    print(uneven_numbers)