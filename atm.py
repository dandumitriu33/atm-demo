import sys
import bankaccounts as ba
import atmsettings as atm

accounts = ba.accounts
atmSettings = atm.settings


def insertCard():
    return input("Insert your card> ")


def insertCardPin():
    return input("Insert your PIN> ")


def showWelcomeScreen():
    pass


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
    print("=========================================")
    print("Holder Name     : ", cardDetails['card']['holderName'])
    print("Card Type       : ", cardDetails['card']['type'])
    print("Bank Name       : ", cardDetails['bank']['name'])
    print("Current Account : ", cardDetails['bank']['accountNumber'])
    print("=========================================")


def main():

    cardNumber = insertCard()

    if cardExists(cardNumber) == False:
        stopATMWithMessage('Card Does Not Exist')

    if codeIsValid(cardNumber) == False:
        stopATMWithMessage('Inserted Wrong PIN 3 times.')

    cardDetails = getCardDetails(cardNumber)

    showCardDetails(cardDetails)


if __name__ == "__main__":
    main()
