'''
    This is a simple calcultor program 
    which checks for basic validations 
    and returns the results.
'''

def calculator():
    while True:
        try:
            first = float(input('please enter the first number: '))
            second = float(input('please enter the second number: '))
            operator = input('please enter +,-,*,/: ')
            result = None
            match operator.lower():
                case '+':
                    result = first + second
                case '-':
                    result = first - second
                case '*':
                    result = first * second
                case '/':
                    try:
                        result = first / second
                    except ZeroDivisionError:
                        print('can not divide by zero')
                        continue
                case _:
                    print('invalid operation')
            if result is not None:
                print(f'Result is : {result}')
                while True:
                    choice = input('please type y to continue and n to quit: ').lower()
                    if choice == 'y':
                        break
                    elif choice == 'n':
                        print('Thank you for using the Calculator App. Bye')
                        return
                    else:
                        print('please type only y or n: ')
        except ValueError:
            print('Invalid input')

######################## CALL CALCULATOR

calculator()
