import time as t 

print("welcome to 'what os you should use'")
print('')

t.sleep(2)

print("please answer with yes/no")
print('')

t.sleep(2)


answer = str(input("1.Is your father rich? "))

if answer == 'yes':
    print('')

    print("use apple")

else:
    answer1 = str(input("2.do you care about privacy? "))


    if answer1 == 'no':
        print('')
        print("use windows")

    else:
        print('')
        print("use linux")

