# test = calculate_acb([(100, 10, 10), (-50, 10, 10)])
#     # Auto loan monthly payment tests.
#     print('Auto loan monthly payment tests')
#     print(func.auto_loan_monthly_payment(10000, 0, 10, 3), ': 3389.04')
#     print(func.auto_loan_monthly_payment(21431, 4147, 1.92, 48), ': 374.38')
#     print(func.auto_loan_monthly_payment(44065, 12789, 2.38, 60), ': 553.41')

from pfinance import functions


def test_simple_interest():
    assert functions.simple_interest(100, 0, 10) == 100.00
    assert functions.simple_interest(100, 0.10, 10) == 200.00


def test_compound_interest():
    assert functions.compound_interest(100, 0, 10) == 100.00
    assert round(functions.compound_interest(100, 0.10, 10, 12), 2) == 270.70


def test_future_value_series():
    assert functions.future_value_series(100, 0, 10) == 1000.00
    assert round(functions.future_value_series(100, 0.05, 10, 12), 2) == 15528.23
    assert round(functions.future_value_series(100, 0.05, 10, 12, True), 2) == 15592.93
