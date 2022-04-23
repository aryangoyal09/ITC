# Input from user:
Income = float(input('Enter Gross Income in dollars to the nearest penny: '))
Dependents = float(input('Enter number of Dependents: '))

# Calculations
Taxable_Income = Income - 10000 - (Dependents * 3000)
Tax = Taxable_Income / 5

if (Taxable_Income <= 0):
    print('No Income tax')
else:
    print('Income tax =' , Tax)
