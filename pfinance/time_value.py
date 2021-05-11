'''Time value of money functions'''


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


def future_value_schedule(principal: float, interest_schedule: list[float]) -> float:
    '''
    Returns the future value of an investment based on a schedule of interest rates.

        Parameters:
            principal (float): The intiial investment sum
            interest_schedule (list[float]): Schedule of interest rates per period

        Returns:
            future_value (float): The future value of the investment
    '''
    for interest in interest_schedule:
        principal *= 1 + interest

    return principal
