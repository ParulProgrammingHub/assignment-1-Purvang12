print 'ENTER THE FOLLOWING INFORMATION TO CALCULATE SIMPLE INTEREST' 
amt=input('enter the principal amount')
tm=input('enter the time')
inrt=input('enter interest rate')
def simple_interest(x,y,z):
    return x*y*z/100
print 'simple interest for the given info is',simple_interest(amt,tm,inrt)
print 'Total amount is',simple_interest(amt,tm,inrt)+amt
