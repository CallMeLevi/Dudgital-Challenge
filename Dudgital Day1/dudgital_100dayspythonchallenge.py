#1. Create a nice greeting to welcome your users.
#2. Ask the user for the first word of their choice
#3. Ask the user for the second word.
#4. Combine the two words and show them their proposed brand name.
#5. Count the length of characters in the user brand name
#6. Make sure the input cursor shows on a new line.


while True:
    print('Welcome user, thank you for choosing Dudgital branding agency')
    print('Please enter the first word of your brand name')
    firstBrandName = input()
    if firstBrandName == '':
        print('Invalid input')
    else:
        print('Please enter the second word of your brand name')
        secondBrandName = input()
        
        if secondBrandName == '':
            print('Invalid input')
        else:

            brandName = firstBrandName + secondBrandName
            print(f'Your suggested brandnaame is {brandName}')

            length = len(brandName)
            print(f'Your brand name has {length} characters...so....there you go.')
            input()
