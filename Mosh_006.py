#conditional statements
price = 100000
payment = 0
good_credit = False
bad_credit = True

if good_credit:
    payment = price - 0.1 * price
    print (f'Down payment = ${payment}')

elif bad_credit:
    payment = price - 0.2 * price
    print (f'Down payment = ${payment}')
    
