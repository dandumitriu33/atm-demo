import connection


def get_specific_card_holder_name(card_id):
    return connection.get_card_info(card_id).holder_name


def get_specific_card_type(card_id):
    return connection.get_card_info(card_id).card_type


def get_specific_card_bank_name(card_id):
    return connection.get_card_info(card_id).bank_name


def get_specific_card_account_number(card_id):
    return connection.get_card_info(card_id).account_number


def get_specific_card_balance(card_id):
    return connection.get_card_info(card_id).balance


def get_specific_card_currency(card_id):
    return connection.get_card_info(card_id).currency


def get_specific_card_card_pin(card_id):
    return connection.get_card_info(card_id).card_pin


def get_specific_card_failed_pin_attempts(card_id):
    return connection.get_card_info(card_id).failed_pin_attempts


def calculate_balance(card_id, withdraw_amount):
    current_balance = connection.get_card_info(card_id).balance
    new_balance = current_balance - withdraw_amount
    return new_balance


def update_balance(card_id, remaining_balance):
    connection.update_balance_in_db(card_id, remaining_balance)


def update_failed_pin_attempts(card_id, failed_pin_attempts):
    connection.update_failed_pin_attempts_in_db(card_id, failed_pin_attempts)


def verify_blocked_card(card_id):
    failed_pin_attempts = get_specific_card_failed_pin_attempts(card_id)
    if failed_pin_attempts < 0 or failed_pin_attempts > 2:
        return True
    else:
        return False


def verify_pin(card_id, user_pin):
    db_pin = int(get_specific_card_card_pin(card_id))
    if int(user_pin) == db_pin:
        return True
    else:
        return False
