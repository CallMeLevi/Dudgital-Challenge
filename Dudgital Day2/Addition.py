def addition():
    try:
    
        while True:
            print('Enter a two-digit number (between 10 and 99)')
            user_num = str(input())
            if len(user_num) < 2:
                print('Invalid input, the number must be between 10 and 99')
            elif len(user_num) > 2:
                print('Invalid input, the number must be between 10 and 99')
            else:
                x = int(user_num[0])
                y = int(user_num[1])
                print(x + y)
    except ValueError:
            print('Invalid input, You must input two numbers')

addition()
