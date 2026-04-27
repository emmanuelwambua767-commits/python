year=int(input('Enter year: '))
if year%100 == 0:
    print('Century year')
elif year%4 == 0:
    print('Leap year')
else:
    print('Common year')