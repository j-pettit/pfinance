def simple_interest(principle: float, interest_rate: float, periods: int) -> float:
    '''
    Returns the total value of an investment earning simple interest.

        Parameters:
            principle (float): Present value of the investment
            interest_rate (float): The interest rate per investment period, e.g. year
            periods (int): The term of the investment, e.g. years

        Returns:
            future_value (float): The value of the investment after the term
    '''
    interest = interest_rate * periods
    return principle * (1 + interest)


def compound_interest(principle: float, rate_per_period: float, periods: int, compoundings_per_period: int) -> float:
    effective_rate = rate_per_period / compoundings_per_period
    total_periods = periods * compoundings_per_period
    return principle * ((1 + effective_rate) ** total_periods)


def future_value_series(payment, rate_per_period, periods, compoundings_per_period, start_of_period=False):
    effective_rate = rate_per_period / compoundings_per_period
    total_periods = periods * compoundings_per_period
    start_of_period_modifier = 1
    if start_of_period:
        start_of_period_modifier = 1 + effective_rate
    return payment * ((((1 + effective_rate) ** total_periods) - 1) / (effective_rate)) * start_of_period_modifier


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
