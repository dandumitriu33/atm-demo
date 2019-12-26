import connection


def get_specific_card_holder_name(card_id):
    return connection.get_card_info(card_id).holder_name


def get_specific_card_type(card_id):
    return connection.get_card_info(card_id).card_type


def get_specific_card_bank_name(card_id):
    return connection.get_card_info(card_id).bank_name


def get_specific_card_account_number(card_id):
    return connection.get_card_info(card_id).account_number
