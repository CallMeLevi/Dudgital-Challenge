print('Enter your Firstname')
firstName = input()
print('Enter your Lastname')
lastName = input()

fullName = firstName + ' ' + lastName

print(f'Your name is {fullName}')

temporaryValue = firstName
firstName = lastName
lastName = temporaryValue

newFullName = firstName + ' ' + lastName
print(f'Or {newFullName} when written in reverse')
