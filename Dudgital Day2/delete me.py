def add():


    try:
        print('first number please')
        first = int(input())
        print('now second number')
        second = int(input())
        print(first + second)
    except ValueError:
        print('Invalid input mate')

add()
