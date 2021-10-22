def ageCounter():
    try:
        print('How old are you now?')
        currentAge = int(input())
        if currentAge > 90:
            print('Move along old timer, you are way past your time on earth')
        else:
            yearsLeft = 90 - currentAge
            daysLeft = yearsLeft * 365
            weeksLeft = daysLeft / 7
            monthsLeft = daysLeft / 12
            print(f'You have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months and {yearsLeft} years left till you reach 90.')
    except UnboundLocalError:
        print('You have to enter your age or any valid number')

    except ValueError:
        print('You have to enter your age or any valid number')
        
    
ageCounter()
