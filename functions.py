def simple_interest(principle, rate_per_period, periods):
    interest = rate_per_period * periods
    return principle * (1 + interest)

def compound_interest(principle, rate_per_period, periods, compoundings_per_period):
    effective_rate = rate_per_period / compoundings_per_period
    total_periods = periods * compoundings_per_period
    return principle * ((1 + effective_rate) ** total_periods)

print('run tests')
print(simple_interest(100, 0.10, 10), '200')
print(compound_interest(100, 0.10, 10, 12), '270.70')