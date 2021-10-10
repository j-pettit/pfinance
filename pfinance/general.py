'''Common finance functions'''
import math


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


def equivalent_interest_rate(present_value: float, future_value: float, periods: int) -> float:
    '''
    Returns the equivalent interest rate for the growth of an investment.

        Parameters:
            present_value (float): The present value of the investment
            future_value (float): The future value of the investment
            periods (int): The number of periods elapsed between the future and present value

        Returns:
            equivalent_interest_rate (float): The equivalent interest rate
    '''
    return (future_value / present_value) ** (1 / periods) - 1


def loan_payment_schedule(
    principal: float,
    interest_rate: float,
    payment_frequency: int,
    term: int,
    down_payment: float = 0,
) -> dict[str, list[float]]:
    '''
    Returns the payment schedule for a loan.

        Parameters:
            principal (float): Initial value of the loan
            interest_rate (float): Interest rate per period, e.g. year
            payment_frequency (int): Number of payments and compoundings per period, e.g. year
            term (int): Term of the loan in number of payments
            down_payment (float): Amount paid towards the loan before interest, default 0

        Returns:
            loan_payment_schedule (dict):
                principal_payment (list[float]): Portion of the loan payment used to pay the principal
                interest_payment (list[float]): Portion of the loan payment used to pay the interest
                remaining_balance (list[float]): Remaining loan balance after payment
    '''
    payment = loan_payment(principal, interest_rate, payment_frequency, term, down_payment)
    loan_amount = principal - down_payment
    principal_payment, interest_payment, remaining_balance = [], [], []

    for _ in range(term):
        interest_payment.append(loan_amount * interest_rate / payment_frequency)
        principal_payment.append(payment - interest_payment[-1])
        remaining_balance.append(loan_amount - principal_payment[-1])
        loan_amount -= principal_payment[-1]

    return {
        'principal_payment': principal_payment,
        'interest_payment': interest_payment,
        'remaining_balance': remaining_balance,
    }


def number_periods_loan(principal: float, interest_rate: float, payment: float) -> float:
    '''
    Returns the number of periods required to payback a loan with fixed payments.

        Parameters:
            principal (float): Initial value of the loan
            interest_rate (float): Interest rate per period, e.g. year
            payment (float): Constant payment per period, must be negative

        Returns:
            number_periods (float): Number of periods to payback the loan, -1 if loan can not be paid off
    '''
    # Check if loan can be paid back
    if payment <= (principal * interest_rate):
        return -1

    return math.log10(payment / (payment - principal * interest_rate)) / math.log10(1 + interest_rate)


def sum_product(*args: list[float]) -> float:
    '''
    Returns the sum of lists multiplied by eachother. For example, [3, 5, 6, 1] and [4, 2, 7, 8] returns
    (3 * 4) + (5 * 2) + (6 * 7) + (1 * 8) = 72.

        Parameters:
            *lst_args (list[float]): Any number of lists to be multiplied and summed together

        Returns:
            total_sum (float): Total sum of the lists multiplied together. None if lists are different lengths or no
                               lists passed in

    '''
    if len({len(i) for i in args}) != 1:  # Use set comprehension to check if list lengths are same
        return None

    total_sum = 0
    multiplied = 1
    len_list = len(args[0])

    for i in range(len_list):
        for lst in args:
            multiplied *= lst[i]

        total_sum += multiplied
        multiplied = 1

    return total_sum


def sum_squares(vals: list[float]) -> float:
    '''
    Returns the sum of the square of each value in a list. For example, [5,2,1,3] gives 5^2 + 2^2 + 1^2 + 3^2 = 39.

        Parameters:
            vals (list[float]): List of values

        Returns:
            total_sum (float): Sum of squares of values in list.
    '''
    total_sum = 0

    for val in vals:
        total_sum += val * val

    return total_sum
