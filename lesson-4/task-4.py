import utils as ut

currency = ut.currency_rates('USD')
print(f'{currency["value"]}, {currency["date"]}')

currency = ut.currency_rates('EUR')
print(f'{currency["value"]}, {currency["date"]}')
