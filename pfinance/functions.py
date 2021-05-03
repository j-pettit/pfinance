def simple_interest(principle: float, interest_rate: float, periods: int) -> float:
    '''
    Returns the total value of an investment earning simple interest.

        Parameters:
            principle (float): Present value of the investment
            interest_rate (float): Interest rate per period, e.g. year
            periods (int): Term of the investment, e.g. years

        Returns:
            future_value (float): Value of the investment after the term
    '''
    interest = interest_rate * periods
    return principle * (1 + interest)


def compound_interest(principle: float, interest_rate: float, periods: int, compounding_frequency: int = 1) -> float:
    '''
    Returns the total value of an investment earning compound interest.

        Parameters:
            principle (float): Present value of the investment
            interest_rate (float): Interest rate per period, e.g. year
            periods (int): Term of the investment, e.g. years
            compounding_frequency (int): Number of compoundings that occur per period, default 1

        Returns:
            future_value (float): Value of the investment after the term
    '''
    return principle * (1 + effective_interest(interest_rate, compounding_frequency)) ** periods


def effective_interest(nominal_rate: float, periods: int) -> float:
    '''
    Returns the effective annual interest rate.

        Parameters:
            nominal_rate (float): The nominal interest rate (i.e. APR)
            periods (int): The number of compounding periods per year

        Returns:
            effective_interest: The effective interest rate
    '''

    return (1 + nominal_rate / periods) ** periods - 1


def future_value_series(
    payment: float,
    interest_rate: float,
    periods: int,
    compounding_frequency: int = 1,
    start_of_period: bool = False,
) -> float:
    '''
    Returns the total value of an future value series earning compound interest with regular additions.

        Parameters:
            payment (float): Value of the regular additions
            interest_rate (float): Interest rate per period, e.g. year
            periods (int): Number of additions and term of the investment, e.g. years
            compounding_frequency (int): Number of compoundings that occur per period, default 1
            start_of_period (bool): Make the payment at the start of each period, default False

        Returns:
            future_value (float): Value of the investment after the term
    '''
    if interest_rate == 0:
        return payment * periods

    effective_rate = interest_rate / compounding_frequency
    total_periods = periods * compounding_frequency
    start_modifier = 1
    if start_of_period:
        start_modifier = 1 + effective_rate
    return payment * start_modifier * (((1 + effective_rate) ** total_periods) - 1) / effective_rate


def present_value(
    payment: float,
    interest_rate: float,
    periods: int,
    future_value: float = 0,
    start_of_period: bool = False,
) -> float:
    '''
    Returns the present value of a loan or investment based on a constant interest rate.

        Parameters:
            payment (float): The regular payment made each period
            interest_rate (float): The interest rate per period, e.g. year
            periods (int): Number of payments made over the term of the investment
            future_value (float): The total cash amount you want to have at the last payment, default 0
            start_of_period (bool): Payment is made at start of each period, default False

        Returns:
            present_value (float): Present value of a loan or investment
    '''
    if interest_rate == 0:
        return (-1 * payment * periods) - future_value

    if start_of_period:
        pv_type = 1
    else:
        pv_type = 0

    numerator = payment * (1 + interest_rate * pv_type) * ((1 + interest_rate) ** periods - 1) / interest_rate + future_value
    denominator = (1 + interest_rate) ** periods

    return -1 * numerator / denominator


def loan_payment(principal: float, interest_rate: float, payment_frequency: int, term: int, down_payment: float = 0) -> float:
    '''
    Returns the periodic payment required to repay a loan accruing compound interest.

        Parameters:
            principal (float): Initial value of the loan
            interest_rate (float): Interest rate per period, e.g. year
            payment_frequency (int): Number of payments and compoundings per period, e.g. year
            term (int): Term of the loan in number of payments
            down_payment (float): Amount paid towards the loan before interest, default 0

        Returns:
            periodic_payment (float): Period loan payment
    '''
    loan_amount = principal - down_payment
    if interest_rate == 0:
        return loan_amount / term

    effective_rate = interest_rate / payment_frequency
    return loan_amount * effective_rate * (1 + effective_rate) ** term / ((1 + effective_rate) ** term - 1)


def discounted_cash_flow(cash_flows: list[float], discount_rate: float) -> float:
    '''
    Returns the discounted cash flow of a series of future cash flows.

        Parameters:
            cash_flows (list[float]): Future cash flows ordered chronologically
            discount_rate (float): Discount rate of the cash flows

        Returns:
            discounted_cash_flow (float): Adjusted present value of the future cash flows
    '''
    dcf = 0
    for i, cf in enumerate(cash_flows):
        dcf += cf / (1 + discount_rate) ** (i + 1)
    return dcf


def modified_internal_rate_of_return(cash_flows: list[float], finance_rate: float, reinvest_rate: float) -> float:
    '''
    Returns the modified internal rate of return for a list of periodic cash flows.
    Considers both the cost of investment and the interest received on reinvested cash.

        Parameters:
            cash_flows (list[float]): List of cash flows ordered chronologically. Must contain at least one positive
                                      and one negative value
            finance_rate (float): The interest rate you pay for money that is borrowed
            reinvest_rate (float): The interest rate you receive for money that is invested

        Returns:
            modified_internal_rate_of_return (float): Decimal value of the MIRR, None for invalid cash flows
    '''
    negative_values = []
    positive_values = []

    for value in cash_flows:
        if value < 0:
            negative_values.append(value)
            positive_values.append(0.0)
        elif value > 0:
            positive_values.append(value)
            negative_values.append(0.0)
        else:
            negative_values.append(0.0)
            positive_values.append(0.0)

    if (len(set(negative_values)) <= 1 or len(set(positive_values)) <= 1):
        return None

    n = len(cash_flows)
    numerator = -1 * discounted_cash_flow(positive_values, reinvest_rate) * (1 + reinvest_rate) ** n
    denominator = discounted_cash_flow(negative_values, finance_rate) * (1 + finance_rate)

    return (numerator / denominator) ** (1 / (n - 1)) - 1


def bond_coupon_rate(face_value: float, payment: float, payment_rate: int = 1) -> float:
    '''
    Returns the coupon rate of a bond.

        Parameters:
            face_value (float): Par value of the bond at issue
            payment (float): Periodic payment from the bond
            payment_rate (int): Payments per interest period, default 1

        Returns:
            coupon_rate (float): Effective interest rate returned by the bond
    '''
    return (payment * payment_rate) / face_value


def dollar_decimal(fractional_dollar: float, fraction: int) -> float:
    '''
    Converts a fractional dollar into a decimal dollar.
    For example, a value of 1.3 with fraction 4 represents 1 + 3/4 = 1.75.

        Parameters:
            fractional_dollar (float): A number expressed as an integer portion and a fractional
                                       portion, separated by a decimal
            fraction (int): The denominator of the fractional portion, must be positive

        Returns:
            decimal_dollar (float): The dollar decimal representation of the fractional dollar
    '''
    fraction_length = len(str(fraction))
    integer_part = int(fractional_dollar)
    mantissa_part = (fractional_dollar - integer_part) * 10 ** fraction_length

    return(integer_part + mantissa_part / fraction)


def dollar_fractional(decimal_dollar: float, fraction: int) -> float:
    '''
    Converts a decimal dollar into a fractional dollar.
    For example, a value of 1.125 with fraction 16 repesents 1 + 12.5/100 = 1 + 2/16 = 1.02.

        Parameters:
            decimal_dollar (float): The decimal representation of the number
            fraction (int): The denominator of the fractional portion, must be positive

        Returns:
            fractional_dollar (float): The dollar fractional representation of the decimal dollar
    '''
    fraction_length = len(str(fraction))
    integer_part = int(decimal_dollar)
    mantissa_part = (decimal_dollar - integer_part) / 10 ** fraction_length

    return(integer_part + mantissa_part * fraction)


def straight_line_depreciation(purchase_price: float, salvage_value: float, useful_life: int) -> float:
    '''
    Calculates the constant periodic depreciation of an asset.

        Parameters:
            purchase_price (float): The total amount paid for the asset
            salvage_value (float): The value of the asset after its useful life
            useful_life (int): The expected lifespan of an asset in periods, must be greater than 0

        Returns:
            periodic_depreciation (float): The periodic decrease in value of the asset
    '''
    return (purchase_price - salvage_value) / useful_life


def sum_of_years_depreciation(purchase_price: float, salvage_value: float, useful_life: int) -> dict[str, list[float]]:
    '''
    Calculates the depreciation of an asset using sum of years depreciation.

        Parameters:
            purchase_price (float): The total amount paid for the asset
            salvage_value (float): The value of the asset after its useful life
            useful_life (int): The expected lifespan of an asset, must be greater than 0

        Returns:
            sum_of_years_result (dict):
                asset_value (list[float]): Value of the asset at the beginning of the period
                periodic_depreciation (list[float]): Depreciation of the asset at the end of the period
    '''
    total_years = useful_life * (useful_life + 1) / 2
    asset_value = [float(purchase_price)]
    periodic_depreciation = [0.0]

    for i in range(useful_life, 0, -1):
        current_depreciation = (purchase_price - salvage_value) * i / total_years
        periodic_depreciation.append(current_depreciation)
        asset_value.append(asset_value[-1] - current_depreciation)

    return {
        'asset_value': asset_value,
        'periodic_depreciation': periodic_depreciation
    }


def double_declining_balance_depreciation(
    purchase_price: float,
    salvage_value: float,
    useful_life: int,
    factor: float = 2.0,
) -> dict[str, list[float]]:
    '''
    Calculates the depreciation of an asset using double declining balance.

        Parameters:
            purchase_price (float): The total amount paid for the asset
            salvage_value (float): The value of the asset after its useful life
            useful_life (int): The expected lifespan of an asset, must be greater than 0
            factor (int): The rate at which the balance declines, default 2

        Returns:
            double_declining_balance_result (dict):
                asset_value (list[float]): Value of the asset at the beginning of the period
                periodic_depreciation (list[float]): Depreciation of the asset at the end of the period
    '''
    asset_value = [float(purchase_price)]
    periodic_depreciation = [0.0]
    total_depreciation = 0.0

    for _ in range(useful_life):
        current_depreciation = max(
            0,
            min(
                (purchase_price - total_depreciation) * factor / useful_life,
                purchase_price - salvage_value - total_depreciation,
            )
        )

        periodic_depreciation.append(current_depreciation)
        total_depreciation += current_depreciation
        asset_value.append(asset_value[-1] - current_depreciation)

    return {
        'asset_value': asset_value,
        'periodic_depreciation': periodic_depreciation,
    }


def units_of_production_depreciation(
    purchase_price: float,
    salvage_value: float,
    useful_life: int,
    units_produced: int,
) -> float:
    '''
    Calculates the depreciation for a given period using units of production depreciation.

        Parameters:
            purchase_price (float): The total amount paid for the asset
            salvage_value (float): The value of the asset after its useful life
            useful_life (int): The total number of units the asset is expected to produce
            units_produced (int): The number of units produced by the asset during a single period

        Returns:
            depreciation (float): The depreciation of the asset for a single period
    '''
    return (units_produced / useful_life) * (purchase_price - salvage_value)


def norberts_gambit(
    quantity: int,
    purchase_price: float,
    sale_price: float,
    rate: float = 1,
    purchase_commission: float = 0,
    sale_commission: float = 0,
) -> dict[str, float]:
    '''
    Returns the converted value and capital gain of an execution of Norbert's Gambit.

        Parameters:
            quantity (int): Number of securities transacted
            purchase_price (float): Unit price of the purchased securities
            sale_price (float): Unit price of the sold securities
            rate (float): Exchange rate between the purchasing currency and the sale currency expressed as a multiplier of the
                          purchasing currency, default 1
            purchase_commission (float): Commission paid in the purchasing currency on the purchase transaction, default 0
            sale_commission (float): Commission paid in the sale currency on the sale transaction, default 0

        Returns:
            gambit_result (dict):
                base_value (float): Final value of the conversion expressed in the purchase currency
                base_gain (float): Capital gain of the conversion expressed in the purchase currency
                converted_value (float): Final value of the conversion expressed in the sale currency
                converted_gain (float): Capital gain of the conversion expressed in the sale currency
    '''
    initial_value = quantity * purchase_price - purchase_commission
    final_value = quantity * sale_price - sale_commission

    return {
        'base_value': final_value / rate,
        'base_gain': (final_value / rate) - initial_value,
        'converted_value': final_value,
        'converted_gain': final_value - (initial_value * rate),
    }


class adjusted_cost_base:
    '''
    Represents an adjusted cost base tracker

    Methods:
        buy(quantity, unit_price, commission): Records a purchase transaction
        sell(quantity, unit_price, commission): Records a sale transaction
        get_acb(): Returns the adjusted cost base of the position
    '''
    def __init__(self):
        '''
        Constructs the necessary attributes for the adjusted cost base tracker object.
        '''
        self._book_value = 0
        self._acb = 0
        self._shares = 0

    def buy(self, quantity: int, unit_price: float, commission: float = 0):
        '''
        Records a purchase transaction.

        Parameters:
            quantity (int): Number of securities purchased
            unit_price (float): Price per security paid
            commission (float): Commission paid in the transaction, default 0
        '''
        self._shares += quantity
        self._book_value += quantity * unit_price + commission
        self._acb = self._book_value / self._shares

    def sell(self, quantity: int, unit_price: float, commission: float = 0) -> float:
        '''
        Records a sale transaction.

        Parameters:
            quantity (int): Number of securities sold
            unit_price (float): Price per security received
            commission (float): Commission paid in the transaction, default 0

        Returns:
            capital_gain (float): The capital gain on the sale
        '''
        self._shares -= quantity
        capital_gain = (quantity * unit_price - commission) - (quantity * self._acb)
        if self._shares == 0:
            self._book_value = 0
            self._acb = 0
        else:
            self._book_value -= quantity * self._acb
        return capital_gain

    def get_acb(self) -> float:
        '''
        Returns the adjusted cost base of the position

        Returns:
            acb (float): Adjusted cost base of the position
        '''
        return self._acb
