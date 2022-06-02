import sys
import utils as ut

currency = ut.currency_rates(str(sys.argv[1]))
print(f'{currency["value"]}, {currency["date"]}')
