'''Unit and notation conversion functions'''


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


def percent_to_basis(percent: float) -> float:
    '''
    Converts a percentage to the equivalent number of basis points.

    Parameters:
        percent (float): Percentage value expressed in decimal notation

    Returns:
        basis_points (float): Equivalent number of basis points
    '''
    return percent * 10000


def increase_to_basis(starting_value: float, final_value: float) -> float:
    '''
    Converts a value increase to the equivalent number of basis points.

    Parameters:
        starting_value (float): Initial value of the asset
        final_value (float): Final value of the asset

    Returns:
        basis_points (float): Equivalent number of basis points
    '''
    return (final_value / starting_value - 1) * 10000


def basis_to_percent(basis_points: float) -> float:
    '''
    Converts basis points to the equivalent percentage.

    Parameters:
        basis_points (float): Number of basis points

    Returns:
        percent (float): Equivalent percentage expressed in decimal notation
    '''
    return basis_points / 10000
