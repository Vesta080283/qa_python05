from datetime import date

user_name = input('Enter your name: ')
yob = int(input('Enter your birthday year: '))
age = date.today().year - yob
message = 'Hello'
print(f'{message}, {user_name}. Your age is: {age}')
