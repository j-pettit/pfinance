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
