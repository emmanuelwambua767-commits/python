# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
user1=input('enter number: ')
user2=input('enter number: ')
user3=input('enter number: ')
if user1>=user2 and user1>=user3:
    largest=user1
elif user2>=user1 and user2>=user3:
    largest=user2
else:
    largest=user3
print(type(input))
print('the largest number:',largest)
user1=int(input('enter number: '))
user2=int(input('enter number: '))
user3=int(input('enter number: '))
user4=int(input('enter number: '))
if user1>=user2 and user1>=user3 and user1>=user4:
    largest=user1
elif user2>=user1 and user2>=user3 and user2>=user4:
    largest=user2
elif user3>=user1 and user3>=user2 and user3>=user4:
    largest=user3
else:
    largest=user4
print('the largest number: ',largest)
# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temperature=int(input('enter temperature: '))
if temperature>30:
    print('The temperature is too high.')
elif temperature>=15 and temperature<30:
    print('Normal Temperature.')
else:
    print('Cold Temperature.')
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=10 and 20
y=100
if x>=10 and y>=100:
    print('Conditions met')
else:
    print('Conditions not met')
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password='secret123'
if password=='secret123':
    print('Access granted')
else:
    print('Access Denied')
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
studentscore=100
attendance=100
if studentscore>=90 and attendance>80:
    print('Excellent student')
else:
    print('Good score, but attendance needs improvement')
#          Attempt the questions in the link below
# https://realpython.com/quizzes/python-conditional-statements/
 