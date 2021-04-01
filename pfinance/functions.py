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
