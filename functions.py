def simple_interest(principle, rate_per_period, periods):
    interest = rate * period
    return principle * (1 + interest)

def compount_interest(principle, rate_per_period, periods, compoundings_per_period):
    effective_rate = rate_per_period / compoundings_per_period
    total_periods = periods * compoundings_per_period
    return principle * ((1 + effective_rate) ** total_periods)

