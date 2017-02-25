print 'ENTER THE FOLLOWING INFORMATION TO CALCULATE COMPOUND INTEREST' 
amt=input('enter the principal amount')
tm=input('enter the time')
inrt=input('enter interest rate')
n=input('enter the number of times the interest is comound per year')
def compound_interest(w,x,y,z):
    return w*(1+y/z)**(z*x)
print 'compound interest for the given info is',compound_interest(amt,tm,inrt,n)
print 'Total amount is',compound_interest(amt,tm,inrt,n)+amt
