p = float(input('Initial principal amount: '))
t = float(input('Number of years for the loan: '))
r = float(input('Annual nominal interest rate: '))
n = float(input('Number of times interest is compounded per year: '))
a = p * (1 + (r / n)) ** (n * t)
print('Total amount is: ', a)