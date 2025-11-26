hours = float( input ( ' Enter hours:'))
rate = float( input( ' Enter rate:'))
def computepay ( hours, rate):
    if hours<= 40:
        pay = hours * rate
    elif hours>= 40:
        pay = 40* rate + ( hours - 40) * rate * 1.5
    return pay
luong= computepay( hours, rate)
print (' Pay:', luong)