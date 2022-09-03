### Monthly Payment
# import numpy as np
# https://pythontic.com/finance/numpy/pmt
# https://www.statology.org/python-monthly-payment-function/
# https://stackoverflow.com/questions/1525611/python-smarter-way-to-calculate-loan-payments
# https://superuser.com/questions/871404/what-would-be-the-the-mathematical-equivalent-of-this-excel-formula-pmt
AR=0.0310
BP=120000
LL=10
R=(1+AR)**(1/12)-1
monthly_payment=(R)*(1/(1-(1+R)**(-LL*12)))*BP
print("monthly_payment: ",monthly_payment)

### RATE

# https://numpy.org/doc/1.17/reference/generated/numpy.rate.html
#https://github.com/numpy/numpy/blob/v1.17.5/numpy/lib/financial.py#L580-L650
# https://www.geeksforgeeks.org/numpy-rate-in-python/
# https://numpy.org/numpy-financial/latest/rate.html
# https://superuser.com/questions/1121889/how-do-i-reproduce-the-excel-function-rate-in-any-programming-language-e-g-ruby
BP=120000
LL=13
PMT=960

# import numpy_financial as npf

# r=npf.rate(12,200000,200,0)
maxiter=1000000
nper=LL*12
pmt=PMT
pv=BP
tolerancy = 0.000001
def rate(nper, pmt, pv, fv = 0, end_or_beginning = 0, rate_guess = 0.10):
      guess = rate_guess
      close = False
      iterator = 0
      while (iterator < maxiter) and not close:
        temp = newton_iter(guess, nper, pmt, pv, fv, end_or_beginning)
        next_guess = round(guess - temp,20)
        diff = abs(next_guess - guess)
        close = diff < tolerancy
        guess = next_guess
        iterator += 1
      return next_guess

def newton_iter(r, n, p, x, y, w):
      t1 = (r+1)**n
      t2 = (r+1)**(n-1)
      return ((y + t1*x + p*(t1 - 1)*(r*w + 1)/r) / (n*t2*x - p*(t1 - 1)*(r*w + 1)/(r**2) + n*p*t2*(r*w + 1)/r + p*(t1 - 1)*w/r))

r=rate(LL*12, -PMT, BP)    
print("r: ",r)
ar=(1+r)**12 -1
print("ar: ",ar)

### PERIODS

AR=0.0310
R=(1+AR)**(1/12)-1
PMT=1100
def ln(x):
    n = 10000.0
    return n * ((x ** (1/n)) - 1)

def periods(rate, pmt, pv, fv = 0, end_or_beginning = 0):
      if rate==0:
          return (-pv - fv) / pmt 
      else:
          z = pmt * (1 + rate * end_or_beginning) / rate
          temp = ln((-fv + z) / (pv + z))
          return temp / ln(1 + rate)
      
nper=periods(R, -PMT, BP) # ==> 64.07334877066185
print("nper: ",nper)
ynper=nper/12
print("ynper: ",ynper)

### Interest Reimbursement

#https://gist.github.com/raadk/dcd503815bbb271484ff
#https://gist.github.com/ghalimi/4590988
LL=10
def finalvalue(rate, nper, pmt, pv, end_or_beginning = 0):
      temp = (1 + rate) ** nper
      fact = (1 + rate* end_or_beginning) * (temp - 1) / rate
      return -(pv * temp + pmt * fact)
def ipmt(rate, per, nper, pv, fv = 0, end_or_beginning = 0):
      pmt = -(rate)*(1/(1-(1+rate)**(-nper)))*pv #(R)*(1/(1-(1+R)**(-LL*12)))*BP
      fv = finalvalue(rate, (per - 1), pmt, pv, end_or_beginning) * rate
      if end_or_beginning == 1:
          temp =  fv / (1 + rate) 
      else: 
          temp=fv
      return temp
 
ip=ipmt(R, 1, LL*12, BP)
pp=-(monthly_payment-abs(ip))
print("ip: ",ip)
print("pp: ",pp)

### Cumulated Interest Reimbursement

def cum_ipmt(rate, start_per,end_per, nper, pv, fv = 0, end_or_beginning = 0):
    cum_ip=0
    for i in range(start_per,end_per+1):
        cum_ip-=ipmt(rate, i, nper, pv)
        # print(ipmt(rate, i, nper, pv))
        # print(i)
    return cum_ip
        
cum_ip=cum_ipmt(R, 1,12, LL*12, BP)
cum_pp=monthly_payment*12-cum_ip
print("cum_ip: ",cum_ip)
print("cum_pp: ",cum_pp)
print("cum_tot: ",cum_ip+cum_pp)

### SCHEDULE

AR=0.0310
BP=120000
LL=10
R=(1+AR)**(1/12)-1

periods=[i for i in range(1,LL*12+1)]
payments=[(R)*(1/(1-(1+R)**(-LL*12)))*BP for i in range(1,LL*12+1)]
interest=[ipmt(R,i,LL*12,BP) for i in range(1,LL*12+1)]
capital=[(payments[i-1]+interest[i-1]) for i in range(1,LL*12+1)]
residual=[[] for i in range(0,LL*12)]
residual[0]=BP-capital[0]
for i in range(1,LL*12):
        residual[i]=residual[i-1]-capital[i]
    

