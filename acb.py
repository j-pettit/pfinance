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

test = calculate_acb([(100, 10, 10), (-50, 10, 10)])
print(test)