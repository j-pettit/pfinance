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


def test_loan_payment():
    assert functions.loan_payment(1000, 0, 1, 10) == 100.00
    assert round(functions.loan_payment(100000, 0.10, 12, 60), 2) == 2124.70
    assert round(functions.loan_payment(150000, 0.10, 12, 60, 50000), 2) == 2124.70
