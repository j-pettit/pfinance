# if __name__ == '__main__':
#     print('run tests')
#     print(f'{simple_interest(100, 0.10, 10):.2f} : 200.00')
#     print(f'{compound_interest(100, 0.10, 10, 12):.2f} : 270.70')
#     print(f'{future_value_series(100, 0.05, 10, 12):.2f} : 15528.23')
#     print(f'{future_value_series(100, 0.05, 10, 12, True):.2f} : 15592.93')

from py-finance import functions # this doesn't work, modules with -?

def test_simple_interest():
    assert functions.simple_interest(100, 0.10, 10) == 200.0