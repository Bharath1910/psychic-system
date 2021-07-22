while True:

    print("1.centimeters")
    print("2.Feets")
    print("3.meters")

    a = int(input("which unit of height do you want?:"))


    if a == 1:
        x = float(input("enter your height in centimeters:"))
        y = float(input("enter your weight in Kg:"))

        c = x/100

        d = y/c**2

        print(d)

        if d >= 25:
            print('you are over weight,please consult a docter')

        elif d <= 18:
            print('you are underweight,just eat more ;)')

        else:
            print('you are healthy')

        print('')

    elif a == 2:
        q = float(input("enter your height in feets:"))
        y = float(input("enter your weight in Kg:"))

        r = q/3.3

        r = y/q**2

        print(r)

        if r >= 25:
            print('you are over weight,please consult a docter')

        elif r <= 18:
            print('you are underweight,just eat more ;)')

        else:
            print('you are healthy')

        print('')

    elif a==3:
        f = float(input("enter your hieght in meteres:"))
        y = float(input("enter your weight in Kg:"))

        r = y/f**2

        print(y)

        if y >= 25:
            print('you are over weight,please consult a docter')

        elif y <=18:
            print('you are underweight,Please consult a docter')

        else:
            print('you are healthy')

        print('')