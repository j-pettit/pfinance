'''Securities tracking and analysis functions'''


def bond_coupon_rate(face_value: float, payment: float, payment_rate: int = 1) -> float:
    '''
    Returns the coupon rate of a bond.

        Parameters:
            face_value (float): Par value of the bond at issue
            payment (float): Periodic payment from the bond
            payment_rate (int): Payments per interest period, default 1

        Returns:
            coupon_rate (float): Effective interest rate returned by the bond
    '''
    return (payment * payment_rate) / face_value


def norberts_gambit(
    quantity: int,
    purchase_price: float,
    sale_price: float,
    rate: float = 1,
    purchase_commission: float = 0,
    sale_commission: float = 0,
) -> dict[str, float]:
    '''
    Returns the converted value and capital gain of an execution of Norbert's Gambit.

        Parameters:
            quantity (int): Number of securities transacted
            purchase_price (float): Unit price of the purchased securities
            sale_price (float): Unit price of the sold securities
            rate (float): Exchange rate between the purchasing currency and the sale currency expressed as a multiplier of the
                          purchasing currency, default 1
            purchase_commission (float): Commission paid in the purchasing currency on the purchase transaction, default 0
            sale_commission (float): Commission paid in the sale currency on the sale transaction, default 0

        Returns:
            gambit_result (dict):
                base_value (float): Final value of the conversion expressed in the purchase currency
                base_gain (float): Capital gain of the conversion expressed in the purchase currency
                converted_value (float): Final value of the conversion expressed in the sale currency
                converted_gain (float): Capital gain of the conversion expressed in the sale currency
    '''
    initial_value = quantity * purchase_price - purchase_commission
    final_value = quantity * sale_price - sale_commission

    return {
        'base_value': final_value / rate,
        'base_gain': (final_value / rate) - initial_value,
        'converted_value': final_value,
        'converted_gain': final_value - (initial_value * rate),
    }


class adjusted_cost_base:
    '''
    Represents an adjusted cost base tracker

    Methods:
        buy(quantity, unit_price, commission): Records a purchase transaction
        sell(quantity, unit_price, commission): Records a sale transaction
        get_acb(): Returns the adjusted cost base of the position
    '''
    def __init__(self):
        '''
        Constructs the necessary attributes for the adjusted cost base tracker object.
        '''
        self._book_value = 0
        self._acb = 0
        self._shares = 0

    def buy(self, quantity: int, unit_price: float, commission: float = 0):
        '''
        Records a purchase transaction.

        Parameters:
            quantity (int): Number of securities purchased
            unit_price (float): Price per security paid
            commission (float): Commission paid in the transaction, default 0
        '''
        self._shares += quantity
        self._book_value += quantity * unit_price + commission
        self._acb = self._book_value / self._shares

    def sell(self, quantity: int, unit_price: float, commission: float = 0) -> float:
        '''
        Records a sale transaction.

        Parameters:
            quantity (int): Number of securities sold
            unit_price (float): Price per security received
            commission (float): Commission paid in the transaction, default 0

        Returns:
            capital_gain (float): The capital gain on the sale
        '''
        self._shares -= quantity
        capital_gain = (quantity * unit_price - commission) - (quantity * self._acb)
        if self._shares == 0:
            self._book_value = 0
            self._acb = 0
        else:
            self._book_value -= quantity * self._acb
        return capital_gain

    def get_acb(self) -> float:
        '''
        Returns the adjusted cost base of the position

        Returns:
            acb (float): Adjusted cost base of the position
        '''
        return self._acb
