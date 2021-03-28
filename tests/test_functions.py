# if __name__ == '__main__':
#     print('run tests')
#     print(f'{simple_interest(100, 0.10, 10):.2f} : 200.00')
#     print(f'{compound_interest(100, 0.10, 10, 12):.2f} : 270.70')
#     print(f'{future_value_series(100, 0.05, 10, 12):.2f} : 15528.23')
#     print(f'{future_value_series(100, 0.05, 10, 12, True):.2f} : 15592.93')

# test = calculate_acb([(100, 10, 10), (-50, 10, 10)])
# print(test)

# This file is just for testing the functions. It can probably be removed once 
# we figure out how to make this into a package.

# import pfinance.functions as func

# if __name__ == '__main__':
#     # Simple interest tests.
#     print('Simple interest tests')
#     print(f'{func.simple_interest(100, 0.10, 10):.2f} : 200.00')

#     # Compound interest tests.
#     print('Compound interest tests')
#     print(f'{func.compound_interest(100, 0.10, 10, 12):.2f} : 270.70')

#     # Future value series tests.
#     print('Future series tests')
#     print(f'{func.future_value_series(100, 0.05, 10, 12):.2f} : 15528.23')
#     print(f'{func.future_value_series(100, 0.05, 10, 12, True):.2f} : 15592.93')

#     # Auto loan monthly payment tests.
#     print('Auto loan monthly payment tests')
#     print(func.auto_loan_monthly_payment(10000, 0, 10, 3), ': 3389.04')
#     print(func.auto_loan_monthly_payment(21431, 4147, 1.92, 48), ': 374.38')
#     print(func.auto_loan_monthly_payment(44065, 12789, 2.38, 60), ': 553.41')

from pfinance import functions


def test_simple_interest():
    assert functions.simple_interest(100, 0.10, 10) == 200.0
