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
            compounding_frequency (int): Number of compoundings that occur period, default 1

        Returns:
            future_value (float): Value of the investment after the term
    '''
    effective_rate = interest_rate / compounding_frequency
    total_periods = periods * compounding_frequency
    return principle * ((1 + effective_rate) ** total_periods)


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
            compounding_frequency (int): Number of compoundings that occur period, default 1
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
    return payment * ((((1 + effective_rate) ** total_periods) - 1) / (effective_rate)) * start_modifier


def calculate_acb(transactions):
    total_shares = 0
    book_value = 0
    for t in transactions:
        (shares, price, commission) = t
        if shares > 0:
            total_shares += shares
            book_value += shares * price + commission
        else:
            total_shares += shares
            book_value += shares * price
    return book_value / total_shares


def auto_loan_monthly_payment(vehicle_price, down_payment, interest_apr_percent, loan_term_months):
    # Interest compounded and applied monthly.
    interest_apr = interest_apr_percent / 100
    loan_amount = vehicle_price - down_payment
    numerator = loan_amount * (interest_apr/12) * (1 + interest_apr/12)**loan_term_months
    denominator = (1 + interest_apr/12)**loan_term_months - 1
    return round(numerator / denominator, 2)
