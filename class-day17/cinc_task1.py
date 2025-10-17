'''
number_val1 = input("enter your number")
number_val = input("enter your number")

if(number_val % 2 == 0 and number_val % 5 == 0):
    print('Even and divisible by 5')
else:
    print('Odd')
'''



person_age = int(input("Please enter your age :"))

if person_age >= 18:
    cf = input('Do you have National Id card? Y/N:')
    if((cf == 'Y') or (cf == 'y')):
        cnic = input('Please enter your cnic :')
        translate_table = str.maketrans('', '', 'abcdefghijklmnopqrstuvwxyz#$-_')
        cleaned_password = cnic.translate(translate_table)
        print(cleaned_password)
        if(len(cleaned_password) == 13 and cleaned_password.isdigit()):
            print('Welcome, you can vote')
        else:
            print("invalid cnic number")
    else:
        print("Since you don't have CNIC, so you can't vote.")
else:
    print('Your are not eligible for the vote....')


