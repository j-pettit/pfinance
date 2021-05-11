from pfinance import conversion, depreciation, general, securities, time_value


# Helper functions
def _compare_list_float(list1, list2, rounding_precision):
    # Compares two lists of floats after rounding.
    if len(list1) != len(list2):
        print("Lists are different lengths.")
        print("list1 length:", len(list1))
        print("list2 length:", len(list2))
        return False

    for i in range(len(list1)):
        if round(list1[i], rounding_precision) != round(list2[i], rounding_precision):
            print("List index", str(i), "have different values.")
            print("list1[" + str(i) + "] =", round(list1[i], rounding_precision))
            print("list2[" + str(i) + "] =", round(list2[i], rounding_precision))
            return False

    return True


def test_compare_list_float():
    list1 = [1.12, 1.22, 1.32, 1.42]
    list2 = [1.12, 1.22, 1.32]
    list3 = [1.123, 2.123, 3.123, 4.123]
    list4 = [1.123, 2.123, 3.126, 4.123]
    list5 = [2.457, 9.528, 9.65, 4.182]
    list6 = [2.46, 9.53, 9.65, 4.18]
    assert not(_compare_list_float(list1, list2, 1))  # Fail different lengths
    assert not(_compare_list_float(list3, list4, 2))  # Fail different values
    assert _compare_list_float(list5, list6, 2)


# General
def test_simple_interest():
    assert general.simple_interest(100, 0, 10) == 100.00
    assert general.simple_interest(100, 0.10, 10) == 200.00


def test_compound_interest():
    assert general.compound_interest(100, 0, 10) == 100.00
    assert round(general.compound_interest(100, 0.10, 10, 12), 2) == 270.70


def test_effective_interest():
    assert general.effective_interest(0, 12) == 0
    assert round(general.effective_interest(0.05, 12), 6) == 0.051162
    assert round(general.effective_interest(0.0525, 4), 7) == 0.0535427
    assert round(general.effective_interest(1.25, 7), 6) == 2.158576


def test_loan_payment():
    assert general.loan_payment(1000, 0, 1, 10) == 100.00
    assert round(general.loan_payment(100000, 0.10, 12, 60), 2) == 2124.70
    assert round(general.loan_payment(150000, 0.10, 12, 60, 50000), 2) == 2124.70


def test_equivalent_interest_rate():
    assert round(general.equivalent_interest_rate(10000, 11000, 96), 7) == 0.0009933
    assert round(general.equivalent_interest_rate(1000, 10000, 5), 3) == 0.585
    assert round(general.equivalent_interest_rate(700, 300, 12), 4) == -0.0682


def test_loan_payment_schedule():
    principal_payment1 = [162.55, 164.17, 165.82, 167.47, 169.15, 170.84]
    interest_payment1 = [10.0, 8.37, 6.73, 5.07, 3.40, 1.71]
    remaining_balance1 = [837.45, 673.28, 507.46, 339.99, 170.84, 0.00]
    principal_payment2 = [74.02, 74.39, 74.77, 75.14, 75.51, 75.89, 76.27]
    interest_payment2 = [2.63, 2.26, 1.89, 1.51, 1.14, 0.76, 0.38]
    remaining_balance2 = [451.98, 377.58, 302.82, 227.68, 152.16, 76.27, 0.0]
    principal_payment3 = [100.0, 100.0, 100.0, 100.0, 100.0]
    interest_payment3 = [0.0, 0.0, 0.0, 0.0, 0.0]
    remaining_balance3 = [400.0, 300.0, 200.0, 100.0, 0.0]
    assert _compare_list_float(general.loan_payment_schedule(1000, 0.12, 12, 6)['principal_payment'], principal_payment1, 2)
    assert _compare_list_float(general.loan_payment_schedule(1000, 0.12, 12, 6)['interest_payment'], interest_payment1, 2)
    assert _compare_list_float(general.loan_payment_schedule(1000, 0.12, 12, 6)['remaining_balance'], remaining_balance1, 2)
    assert _compare_list_float(general.loan_payment_schedule(526, 0.06, 12, 7)['principal_payment'], principal_payment2, 2)
    assert _compare_list_float(general.loan_payment_schedule(526, 0.06, 12, 7)['interest_payment'], interest_payment2, 2)
    assert _compare_list_float(general.loan_payment_schedule(526, 0.06, 12, 7)['remaining_balance'], remaining_balance2, 2)
    assert _compare_list_float(general.loan_payment_schedule(500, 0, 12, 5)['principal_payment'], principal_payment3, 2)
    assert _compare_list_float(general.loan_payment_schedule(500, 0, 12, 5)['interest_payment'], interest_payment3, 2)
    assert _compare_list_float(general.loan_payment_schedule(500, 0, 12, 5)['remaining_balance'], remaining_balance3, 2)


# Time Value
def test_future_value_series():
    assert time_value.future_value_series(100, 0, 10) == 1000.00
    assert round(time_value.future_value_series(100, 0.05, 10, 12), 2) == 15528.23
    assert round(time_value.future_value_series(100, 0.05, 10, 12, True), 2) == 15592.93


def test_present_value():
    assert time_value.present_value(100, 0, 12, 0, False) == -1200.00
    assert round(time_value.present_value(500, 0.06, 48, 9000, False), 2) == -8374.00
    assert round(time_value.present_value(200, 0.07, 36, 1000, True), 2) == -2877.07


def test_discounted_cash_flow():
    assert time_value.discounted_cash_flow([], 0) == 0.00
    assert round(time_value.discounted_cash_flow([1000, 1000, 4000, 4000, 6000], 0.05), 2) == 13306.73


def test_modified_internal_rate_of_return():
    assert time_value.modified_internal_rate_of_return([], 0.1, 0.1) is None
    assert time_value.modified_internal_rate_of_return([10, 10], 0.1, 0.1) is None
    assert time_value.modified_internal_rate_of_return([-10, -10], 0.1, 0.1) is None
    assert round(time_value.modified_internal_rate_of_return([-120000, 39000, 30000, 21000, 37000], 0.1, 0.12), 3) == 0.063
    assert round(time_value.modified_internal_rate_of_return([24, -96, -52, 27, -17, 15, -2, 0, 0], 0.05, 0.07), 3) == -0.056


def test_future_value_schedule():
    assert round(time_value.future_value_schedule(1000, [0.02, 0.03, 0.04, 0.05]), 2) == 1147.26
    assert round(time_value.future_value_schedule(123.45, [0, 0, 0, 0, 0, 0, 0, 0, 0]), 2) == 123.45
    assert round(time_value.future_value_schedule(15973, [0.02, 0.09, -0.08, 0.2]), 2) == 19605.69


# Conversion
def test_dollar_decimal():
    assert round(conversion.dollar_decimal(1.2, 16), 2) == 2.25
    assert round(conversion.dollar_decimal(9000.4123, 200), 4) == 9002.0615
    assert round(conversion.dollar_decimal(703.238, 23), 5) == 704.03478


def test_dollar_fractional():
    assert (round(conversion.dollar_fractional(1.125, 16), 2)) == 1.02
    assert (round(conversion.dollar_fractional(1.125, 32), 2)) == 1.04
    assert (round(conversion.dollar_fractional(738.526, 29), 5)) == 738.15254


# Depreciation
def test_straight_line_depreciation():
    assert round(depreciation.straight_line_depreciation(2000, 500, 5)) == 300
    assert depreciation.straight_line_depreciation(30000, 7500, 10) == 2250


def test_sum_of_years_depreciation():
    asset_value1 = [1000.0, 673.33, 412.00, 216.00, 85.33, 20.00]
    depreciation1 = [0.0, 326.67, 261.33, 196.00, 130.67, 65.33]
    asset_value2 = [12345, 9339.00, 6762.43, 4615.29, 2897.57, 1609.29, 750.43, 321.00]
    depreciation2 = [0.0, 3006.00, 2576.57, 2147.14, 1717.71, 1288.29, 858.86, 429.43]
    asset_value3 = [100.0, 0.0]
    depreciation3 = [0.0, 100.0]
    assert _compare_list_float(depreciation.sum_of_years_depreciation(1000, 20, 5)['asset_value'], asset_value1, 2)
    assert _compare_list_float(depreciation.sum_of_years_depreciation(1000, 20, 5)['periodic_depreciation'], depreciation1, 2)
    assert _compare_list_float(depreciation.sum_of_years_depreciation(12345, 321, 7)['asset_value'], asset_value2, 2)
    assert _compare_list_float(
        depreciation.sum_of_years_depreciation(12345, 321, 7)['periodic_depreciation'],
        depreciation2,
        2
    )
    assert _compare_list_float(depreciation.sum_of_years_depreciation(100, 0, 1)['asset_value'], asset_value3, 2)
    assert _compare_list_float(depreciation.sum_of_years_depreciation(100, 0, 1)['periodic_depreciation'], depreciation3, 2)


def test_double_declining_balance_depreciation():
    asset_value1 = [10000.0, 6000.0, 3600.0, 2160.0, 2000.0, 2000.0]
    depreciation1 = [0.0, 4000.0, 2400.0, 1440.0, 160.0, 0.0]
    asset_value2 = [20000.0, 10000.0, 5000.0, 2500.0, 1250.00, 1000.0, 1000.0]
    depreciation2 = [0.0, 10000.0, 5000.0, 2500.0, 1250.0, 250.0, 0.0]
    asset_value3 = [100.0, 100.0, 100.0]
    depreciation3 = [0.0, 0.0, 0.0]
    asset_value4 = [100.0, 0.0]
    depreciation4 = [0.0, 100.0]
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(10000, 2000, 5)['asset_value'],
        asset_value1,
        2
    )
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(10000, 2000, 5)['periodic_depreciation'],
        depreciation1,
        2
    )
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(20000, 1000, 6, 3)['asset_value'],
        asset_value2,
        2
    )
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(20000, 1000, 6, 3)['periodic_depreciation'],
        depreciation2,
        2
    )
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(100, 200, 2)['asset_value'],
        asset_value3,
        2
    )
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(100, 200, 2)['periodic_depreciation'],
        depreciation3,
        2
    )
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(100, 0, 1)['asset_value'],
        asset_value4,
        2
    )
    assert _compare_list_float(
        depreciation.double_declining_balance_depreciation(100, 0, 1)['periodic_depreciation'],
        depreciation4,
        2
    )


def test_units_of_production_depreciation():
    assert depreciation.units_of_production_depreciation(25000, 0, 100, 4) == 1000.0
    assert depreciation.units_of_production_depreciation(500000, 20000, 240000, 10000) == 20000.0


def test_declining_balance():
    asset_value1 = [1000.0, 681.0, 463.76, 315.82, 215.07, 146.47, 99.74]
    depreciation1 = [0.0, 319.0, 217.24, 147.94, 100.75, 68.61, 46.72]
    asset_value2 = [500.0, 448.12, 262.15, 153.36, 89.72, 52.48, 30.70, 21.15]
    depreciation2 = [0.0, 51.88, 185.97, 108.79, 63.64, 37.23, 21.78, 9.56]
    asset_value3 = [900.0, 639.08, 321.45, 161.69, 81.33, 40.91, 32.44]
    depreciation3 = [0.0, 260.93, 317.62, 159.76, 80.36, 40.42, 8.47]
    assert _compare_list_float(depreciation.declining_balance(1000, 100, 6)['asset_value'], asset_value1, 2)
    assert _compare_list_float(depreciation.declining_balance(1000, 100, 6)['periodic_depreciation'], depreciation1, 2)
    assert _compare_list_float(depreciation.declining_balance(500, 20, 6, 3)['asset_value'], asset_value2, 2)
    assert _compare_list_float(depreciation.declining_balance(500, 20, 6, 3)['periodic_depreciation'], depreciation2, 2)
    assert _compare_list_float(depreciation.declining_balance(900, 29, 5, 7)['asset_value'], asset_value3, 2)
    assert _compare_list_float(depreciation.declining_balance(900, 29, 5, 7)['periodic_depreciation'], depreciation3, 2)


# Securities
def test_bond_coupon_rate():
    assert securities.bond_coupon_rate(1000, 0) == 0.00
    assert securities.bond_coupon_rate(1000, 10) == 0.01
    assert securities.bond_coupon_rate(1000, 25, 5) == 0.125


def norberts_gambit():
    assert securities.norberts_gambit(0, 0, 0)['base_value'] == 0
    assert securities.norberts_gambit(10, 50, 45)['base_value'] == 450
    assert securities.norberts_gambit(10, 50, 45)['base_gain'] == -50
    assert securities.norberts_gambit(10, 10, 9, 1.1)['base_value'] == 99
    assert securities.norberts_gambit(10, 10, 9, 1.1)['base_gain'] == -1
    assert securities.norberts_gambit(10, 10, 9, 1.1)['converted_value'] == 90
    assert round(securities.norberts_gambit(10, 10, 9, 1.1)['converted_gain'], 2) == 90.91
    assert securities.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['base_value'] == 292.5
    assert securities.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['base_gain'] == -15
    assert securities.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['converted_value'] == 195
    assert securities.norberts_gambit(20, 15, 10, 1.5, 7.5, 5)['converted_gain'] == -10


def test_adjusted_cost_base():
    test_acb = securities.adjusted_cost_base()
    test_acb.buy(10, 10.00, 5.00)
    assert round(test_acb.get_acb(), 2) == 10.50
    assert round(test_acb.sell(5, 15.00, 5.00), 2) == 17.5
    assert round(test_acb.get_acb(), 2) == 10.50
    test_acb.buy(5, 20.00, 5.00)
    assert round(test_acb.get_acb(), 2) == 15.75
    assert round(test_acb.sell(10, 10.00, 5.00), 2) == -62.50
    assert round(test_acb.get_acb(), 2) == 0.00
