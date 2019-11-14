#Has a good name
    #-expressive
    #-can look like a question

#Does only one thing

#returns a value
    #-can make an exception for defs that just print data

#not longer than 50 lines
    #-

#always returns the same value, for the same arguments
    #should not have side effects, like printing, while you also do calculations and return something

##TASKS##

# Make the atm show the following Options:
#     - Show Account Details
#     - Show Account Balance
#     - Show Withdraw Option
#         - Get user to input the withdraw amount
#         - check against atmSettings to see if he is allowed to withdraw the amount
#         - check if he has a balance higher/equal to (withdraw amount + commission)
#             - if he has the right balance, print a receipt on screen containing the following
#                 Country and City of ATM
#                 Address of ATM
#                 Amount of withdraw
#                 Card Number that was used
#
# atmsettings.py is already imported in atm.py - and contains the atm settings
# bankaccounts is already imported in atm.py and contains the bank accounts.

# REMEMBER!
# To write clear functions!