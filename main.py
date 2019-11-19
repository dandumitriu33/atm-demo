import sys
import data.bankaccounts as ba
import data.atmsettings as atm
import os
import time

accounts = ba.accounts
atmSettings = atm.settings


def insertCard():
    return input("Insert your card> ")


def insertCardPin():
    return input("Insert your PIN> ")


def showWelcomeScreen():
    os.system('clear')
    print('''
========================================

         WELCOME TO SILVER BANK
              INSERT CARD


========================================
    ''')


def showIsertPinScreen():
    os.system('clear')
    print('''
========================================


            TYPE YOUR PIN


========================================
    ''')


def showInvalidMessage(message):
    os.system('clear')
    print('''
========================================


'''
          f'             INVALID {message}'
'''


========================================
        ''')


def show_card_blocked():
    os.system('clear')
    print('''
========================================
    THE PIN FOR THIS CARD HAS BEEN
    ENTERED THREE TIMES INCORRECTLY.
    THE CARD IS NOW BLOCKED.
    PLEASE CONTACT YOUR BANKING AGENT.

========================================
    ''')


def showMainMenu():
    os.system('clear')
    print('''
========================================
        SELECT AN OPTION BELOW
1. SHOW CARD DETAILS
2. SHOW BALANCE
3. WITHDRAW
0. EXIT
========================================
    ''')
    user_option = input('Select an option: ')
    return user_option


def showCardDetails(cardNumber):
    os.system('clear')
    card_holder = accounts[cardNumber]['card']['holderName']
    card_type = accounts[cardNumber]['card']['type']
    bank_name = accounts[cardNumber]['bank']['name']
    bank_account_number = accounts[cardNumber]['bank']['accountNumber']
    print('''
========================================
             CARD DETAILS'''
    f'\nHolder Name     : {card_holder}'
    f'\nCard Type       : {card_type}'
    f'\nBank Name       : {bank_name}'
    f'\nCurrent Account : {bank_account_number}'
    '''
========================================"
    ''')


def showBalance(cardno):
    os.system('clear')
    balance = accounts[cardno]['bank']['balance']
    currency = accounts[cardno]['bank']['currency']
    print('''
========================================
        SHOWING BALANCE

'''
          f'          {currency}: {balance}'
'''

0. BACK
========================================
    ''')


def show_withdraw_screen():
    os.system('clear')
    print('''
========================================


          AMOUNT TO WITHDRAW


========================================
    ''')


def show_insufficient_funds():
    os.system('clear')
    print('''
========================================


           INSUFFICIENT FUNDS


========================================
    ''')


def show_atm_limit_exceeded():
    os.system('clear')
    print('''
========================================


      ATM WITHDRAWAL LIMIT EXCEEDED


========================================
    ''')


def show_receipt(cardNumber, amount):
    os.system('clear')
    country = atmSettings['location']['country']
    city = atmSettings['location']['city']
    address = atmSettings['location']['address']
    currency = accounts[cardNumber]['bank']['currency']
    print('''
========================================
            CASH WITHDRAWAL'''
    f'\n{country}, {city}'
    f'\n{address}'
    f'\n{currency}: {amount}'
    f'\nCard number: {cardNumber}'
    '''
========================================"
    ''')


def cardExists(cardNumber):
    # insert function/statement to verify if card is not 'blocked' in DB
    # if card is 'blocked'
    #       show_card_blocked()
    #       main()
    # else:
    return cardNumber in accounts


def cardCodeIsValid(cardNumber, code):
    return accounts[cardNumber]['card']['code'] == code


def codeIsValid(cardNumber):
    cardPin = insertCardPin()
    if cardCodeIsValid(cardNumber, cardPin) is True:
        return True
    return False


def validate_pin(cardNumber):
    pin_attempts = 0
    while pin_attempts < 3:
        showIsertPinScreen()
        evaluation = codeIsValid(cardNumber)
        if evaluation is True:
            return True
        elif evaluation is False and pin_attempts < 2:
            showInvalidMessage('PIN')
            print('Icorrect PIN. Returning to Insert PIN screen in 5 seconds.')
            pin_attempts += 1
            time.sleep(5)
        elif evaluation is False and pin_attempts == 2:
            # block_card function that would send the info to the DB
            show_card_blocked()
            print('Returning to main screen in 10 seconds.')
            time.sleep(10)
            main()
    return False


def withdraw_cash(cardNumber):
    show_withdraw_screen()
    amount = int(input('Please type the withdrawal amount: '))
    card_type = accounts[cardNumber]['card']['type']
    commission = atmSettings['commission'][card_type]
    atm_limit_EUR = atmSettings['location']['maxWithdrawAmount']['EUR']
    atm_limit_USD = atmSettings['location']['maxWithdrawAmount']['USD']
    available_balance = accounts[cardNumber]['bank']['balance']
    if accounts[cardNumber]['bank']['currency'] == 'EUR':
        operation_limit = int(atm_limit_EUR)
    elif accounts[cardNumber]['bank']['currency'] == 'EUR':
        operation_limit = int(atm_limit_USD)
    if amount + commission <= available_balance and amount <= operation_limit:
        # function to update the balance in the DB
        show_receipt(cardNumber, amount)
        input('Press Enter to continue...')
    elif (amount + commission) > available_balance:
        show_insufficient_funds()
        input('Press Enter to continue...')
        run_menu(cardNumber)
    elif amount > operation_limit:
        show_atm_limit_exceeded()
        input('Press Enter to continue...')
        run_menu(cardNumber)
    run_menu(cardNumber)


def run_menu(cardNumber):
    menu_running = True
    while menu_running is True:
        option = showMainMenu()
        if option == '1':
            show_card_details_running = True
            while show_card_details_running is True:
                os.system('clear')
                showCardDetails(cardNumber)
                deatils_show_selection = input('Select 0 to go back to the main menu.')
                if deatils_show_selection == '0':
                    show_card_details_running = False
                else:
                    continue
        if option == '2':
            show_balance_running = True
            while show_balance_running is True:
                os.system('clear')
                showBalance(cardNumber)
                balance_show_selection = input('Select 0 to go back to the main menu.')
                if balance_show_selection == '0':
                    show_balance_running = False
                else:
                    continue
        if option == '3':
            withdraw_cash(cardNumber)
        if option == '0':
            valid_card = False
            valid_pin = False
            menu_running = False
            main()


def main():

    # first step: validating the card exists and is not blocked

    os.system('clear')
    showWelcomeScreen()
    cardNumber = insertCard()
    if cardExists(cardNumber) is False:
        showInvalidMessage('CARD')
        print('Card Does Not Exist. Returning to main screen in 5 seconds.')
        time.sleep(5)
        main()

    # second step: validating the PIN and blocking if it fails 3 times

    if validate_pin(cardNumber) is False:
        main()
    else:

        # after the security information is verified, shows menu

        run_menu(cardNumber)


if __name__ == "__main__":
    main()
