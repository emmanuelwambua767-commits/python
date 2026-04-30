account=input('Select type of account:')
if account=='Standard':
    amount=int(input('Enter amount: '))
    if amount>=500:
        print('Transaction exceeds the limit for Standard accounts.')
    else:
        print('Transaction approved.')
if account=='Premium':
       amount=int(input('Enter amount: '))
       if amount>=1000:
            print('Transaction exceeds the limit for Premium accounts.')
       else:
            print('Transaction approved.')
else:
     print('Wrong account type.')
start_date=input('Enter date: ')
end_date='2025-10-5'
if start_date<end_date:
     print('Valid Period')
elif start_date>end_date:
     print('Invalid Period')
elif start_date==end_date:
     print('One-Day Period')
# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".
str1=input('Enter code: ')
str2=input('Enter code: ')
if (len(str1))>(len(str2)):
     print('str1 is longer.')
elif (len(str1))<(len(str2)) or (len(str1))>(len(str2)):
     print('str2 is longer.')
else:
     print('Both are of equal length.')
# Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = int(input('Enter id:'))
if user_id in valid_ids:
     print('Access Granted')
else:
     print('Access Denied')
# Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.
value=input('Enter code: ')
if type(value)==str:
     print('String Detected.')
elif type(value)!=str or type(value)==int:
     print('Integer Detected')
else:
     print('Unknown Type')
# Given x = 7 and y = 14, write nested conditional statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.
x=int(input('Enter number: '))
y=int(input('Enter number: '))
if x%2==0 and y%2==0:
     print('x and y are both even')
elif y%2==0:
     print('Only y is even')
else:
     print('Neither x nor y are even')