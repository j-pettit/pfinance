def simple_interest(principle, rate_per_period, periods):
    interest = rate_per_period * periods
    return principle * (1 + interest)

def compound_interest(principle, rate_per_period, periods, compoundings_per_period):
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