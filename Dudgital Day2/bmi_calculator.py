def bmiCalculator():
    
    try:
        print('Enter your weight in Kilograms')
        weight = int(input())
        print('Enter your height in Meters')
        height = int(input())
        bmi = str(weight/(height*height))
        print('Your BMI is', bmi)
    except NameError:
        print('Invalid input')
    except ValueError:
        print('Invalid input')


bmiCalculator()


