# program to prompt the user for hours and rate per hour using input to compute gross pay.
#  Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours
def computepay(h, r):
    if h<40:
        pay = h*r 
    elif h>40:
        a = h*r
        b = (h - 40.0)*(r*0.5)
        pay=a +b  
    return pay 
ab= int(input('enter hours: '))
cd= float(input('enter rate: '))
z = computepay(ab,cd)
print('Pay', z)
