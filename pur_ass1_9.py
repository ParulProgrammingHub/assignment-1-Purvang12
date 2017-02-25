sum=0
print('enter marks out of 100')
for i in range(5):
    sum=float(sum+input('enter marks of subject %s'%(i+1)))
mean=float(sum/5);
per=float((sum/500)*100)
print 'mean of five subjects is',mean,'and percentage is',per,'%'
if (per>35):
    print 'PASS'
else:
    print 'FAIL'
