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


def calculate_balance(card_id, withdraw_amount):
    current_balance = connection.get_card_info(card_id).balance
    new_balance = current_balance - withdraw_amount
    return new_balance


def update_balance(card_id, remaining_balance):
    connection.update_balance_in_db(card_id, remaining_balance)
