c = 0
while c < 1:

    x = float(input('your height in meters: '))
    y = float(input('enter your weight in Kg: '))

    z = y/ x ** 2

    print('Your BMI is: {:1.2f}'.format(z))

    if z >= 25:
        print('you are over weight,please consult a docter')

    elif z <= 18:
        print('you are underweight,please consult a docter')

    else:
        print('you are healthy')

    print('')

    