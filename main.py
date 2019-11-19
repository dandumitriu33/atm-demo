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


def showMainMenu():
    os.system('clear')
    print('''
========================================
        SELECT AN OPTION BELOW
1. SHOW ACCOUNT DETAILS
2. SHOW BALANCE
3. WITHDRAW
0. EXIT
========================================
    ''')
    user_option = input('Select an option: ')
    return user_option


def showBalance():
    os.system('clear')
    print('''
========================================
        SHOWING BALANCE

EUR: 400

0. BACK
========================================
    ''')


def cardExists(cardNumber):
    return cardNumber in accounts


def cardCodeIsValid(cardNumber, code):
    return accounts[cardNumber]['card']['code'] == code


def stopATMWithMessage(message):
    print(message)
    sys.exit()


def codeIsValid(cardNumber):

    currentPINTries = 1
    maxPINTries = 3
    while currentPINTries <= maxPINTries:

        cardPin = insertCardPin()

        if True == cardCodeIsValid(cardNumber, cardPin):
            return True

        currentPINTries = currentPINTries + 1

    return False


def getCardDetails(cardNumber):
    return accounts[cardNumber]


def showCardDetails(cardDetails):
    print("========================================")
    print("             SILVER BANK                ")
    print("Holder Name     : ", cardDetails['card']['holderName'])
    print("Card Type       : ", cardDetails['card']['type'])
    print("Bank Name       : ", cardDetails['bank']['name'])
    print("Current Account : ", cardDetails['bank']['accountNumber'])
    print("========================================")


def main():
    os.system('clear')
    showWelcomeScreen()
    cardNumber = insertCard()
    if cardExists(cardNumber) is False:
        showInvalidMessage('CARD')
        print('Card Does Not Exist. Returning to main screen in 5 seconds.')
        time.sleep(5)
        main()
    valid_pin = False
    while valid_pin is False:
        showIsertPinScreen()
        if codeIsValid(cardNumber) is False:
            showInvalidMessage('PIN')
            print('Icorrect PIN. Returning to Insert PIN screen in 5 seconds.')
            time.sleep(5)
        else:
            valid_pin = True
    menu_running = True
    while menu_running is True:
        option = showMainMenu()
        if option == '1':
            show_card_details_running = True
            while show_card_details_running is True:
                os.system('clear')
                cardDetails = getCardDetails(cardNumber)
                showCardDetails(cardDetails)
                deatils_show_selection = input('Select 0 to go back to the main menu.')
                if deatils_show_selection == '0':
                    show_card_details_running = False
                else:
                    continue
        if option == '2':
            show_balance_running = True
            while show_balance_running is True:
                os.system('clear')
                showBalance()
                balance_show_selection = input('Select 0 to go back to the main menu.')
                if balance_show_selection == '0':
                    show_balance_running = False
                else:
                    continue
        if option == '3':
            print('Under construction.')
        if option == '0':
            valid_card = False
            valid_pin = False
            menu_running = False
            main()

if __name__ == "__main__":
    main()
