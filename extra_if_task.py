year=int(input('enter year: '))
if year%4==0:
    print('Leap year')
elif year%100==0:
    print('Century year')
else:
    print('Common year')
temperature=int(input('enter temperature: '))
if temperature<=0:
    print('Freezing')
elif temperature>=1 and temperature<=15:
    print('Cold')
elif temperature>=16 and temperature<=29:
    print('Warm')
else:
    print('Hot')
day_number=int(input('enter number: '))
if day_number>=1:
    print('Weekday')
elif day_number>=6:
    print('Weekend')
else:
    print('Invalid input')
number1=int(input('enter number: '))
number2=int(input('enter number: '))
if number1==number2:
    print('equal number')
elif number1!=number2:
    print('First is greater')
else:
    print('Second is greater')
grades=int(input('enter marks: '))
if grades>=80:
    print('A')
elif grades<80 and grades>=70:
    print('B')
elif grades<70 and grades>=60:
    print('C')
elif grades<60 and grades>=50:
    print('D')
else:
    print('F')
number=int(input('enter number: '))
if number%3:
    print('Fizz')
elif number%5:
    print('Buzz')
elif number%3 and number%5:
    print('FizzBuzz')
else:
    print('print the number:',number)