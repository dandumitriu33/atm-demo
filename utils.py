def validate_withdraw_amount(number):
    MAX_WITHDRAWAL = 400
    BILL_MULTIPLE = 10
    if number in range(10, MAX_WITHDRAWAL + 1) and number % BILL_MULTIPLE == 0:
        return True
    else:
        return False
