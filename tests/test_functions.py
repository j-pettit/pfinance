from pfinance import functions


def test_simple_interest():
    assert functions.simple_interest(100, 0, 10) == 100.00
    assert functions.simple_interest(100, 0.10, 10) == 200.00


def test_compound_interest():
    assert functions.compound_interest(100, 0, 10) == 100.00
    assert round(functions.compound_interest(100, 0.10, 10, 12), 2) == 270.70


def test_effective_interest():
    assert functions.effective_interest(0, 12) == 0
    assert round(functions.effective_interest(0.05, 12), 6) == 0.051162
    assert round(functions.effective_interest(0.0525, 4), 7) == 0.0535427
    assert round(functions.effective_interest(1.25, 7), 6) == 2.158576


def test_future_value_series():
    assert functions.future_value_series(100, 0, 10) == 1000.00
    assert round(functions.future_value_series(100, 0.05, 10, 12), 2) == 15528.23
    assert round(functions.future_value_series(100, 0.05, 10, 12, True), 2) == 15592.93


def test_present_value():
    assert functions.present_value(100, 0, 12, 0, False) == -1200.00
    assert round(functions.present_value(500, 0.06, 48, 9000, False), 2) == -8374.00
    assert round(functions.present_value(200, 0.07, 36, 1000, True), 2) == -2877.07


def test_loan_payment():
    assert functions.loan_payment(1000, 0, 1, 10) == 100.00
    assert round(functions.loan_payment(100000, 0.10, 12, 60), 2) == 2124.70
    assert round(functions.loan_payment(150000, 0.10, 12, 60, 50000), 2) == 2124.70


def test_discounted_cash_flow():
    assert functions.discounted_cash_flow([], 0) == 0.00
    assert round(functions.discounted_cash_flow([1000, 1000, 4000, 4000, 6000], 0.05), 2) == 13306.73


def test_modified_internal_rate_of_return():
    assert functions.modified_internal_rate_of_return([], 0.1, 0.1) is None
    assert functions.modified_internal_rate_of_return([10, 10], 0.1, 0.1) is None
    assert functions.modified_internal_rate_of_return([-10, -10], 0.1, 0.1) is None
    assert round(functions.modified_internal_rate_of_return([-120000, 39000, 30000, 21000, 37000], 0.1, 0.12), 3) == 0.063
    assert round(functions.modified_internal_rate_of_return([24, -96, -52, 27, -17, 15, -2, 0, 0], 0.05, 0.07), 3) == -0.056


def test_bond_coupon_rate():
    assert functions.bond_coupon_rate(1000, 0) == 0.00
    assert functions.bond_coupon_rate(1000, 10) == 0.01
    assert functions.bond_coupon_rate(1000, 25, 5) == 0.125


def test_dollar_decimal():
    assert round(functions.dollar_decimal(1.2, 16), 2) == 2.25
    assert round(functions.dollar_decimal(9000.4123, 200), 4) == 9002.0615
    assert round(functions.dollar_decimal(703.238, 23), 5) == 704.03478


def test_dollar_fractional():
    assert (round(functions.dollar_fractional(1.125, 16), 2)) == 1.02
    assert (round(functions.dollar_fractional(1.125, 32), 2)) == 1.04
    assert (round(functions.dollar_fractional(738.526, 29), 5)) == 738.15254


def norberts_gambit():
    assert functions.norberts_gambit(0, 0, 0)['base_value'] == 0
    assert functions.norberts_gambit(10, 50, 45)['base_value'] == 450
    assert functions.norberts_gambit(10, 50, 45)['base_gain'] == -50
    assert functions.norberts_gambit(10, 10, 9, 1.1)['base_value'] == 99
    assert functions.norberts_gambit(10, 10, 9, 1.1)['base_gain'] == -1
    assert functions.norberts_gambit(10, 10, 9, 1.1)['converted_value'] == 90
    assert round(functions.norberts_gambit(10, 10, 9, 1.1)['converted_gain'], 2) == 90.91
    assert functions.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['base_value'] == 292.5
    assert functions.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['base_gain'] == -15
    assert functions.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['converted_value'] == 195
    assert functions.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['converted_gain'] == -10


def test_adjusted_cost_base():
    test_acb = functions.adjusted_cost_base()
    test_acb.buy(10, 10.00, 5.00)
    assert round(test_acb.get_acb(), 2) == 10.50
    assert round(test_acb.sell(5, 15.00, 5.00), 2) == 17.5
    assert round(test_acb.get_acb(), 2) == 10.50
    test_acb.buy(5, 20.00, 5.00)
    assert round(test_acb.get_acb(), 2) == 15.75
    assert round(test_acb.sell(10, 10.00, 5.00), 2) == -62.50
    assert round(test_acb.get_acb(), 2) == 0.00
