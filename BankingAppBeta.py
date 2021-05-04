# BUILDING A BANKING APP
UserDetails = {}
import random 

# Welcome
def Welcome() :
    print('WELCOME TO THE BANK OF FAOK!')
    WelcomeQuestion = int(input("Do you have a registered accout with us? \n 1. Yes \n 2. No \n"))
    if WelcomeQuestion == 2:
        CreationOfRegisteredAccount ()
    elif WelcomeQuestion == 1:
        Login ()

    else:
        print("Invalid option selected, Try again")
        print ('           ')
        Welcome ()


# Account number generation
def AccountNumberGen():
    print('Your account number is: ')
    return random.randrange(1111111111,9999999999)


# Register phase
def CreationOfRegisteredAccount ():
     print('Register  account')
     global FirstName
     FirstName = input('What is your first name? \n')
     LastName = input('what is your last name? \n')
     Email = input('what is your email? \n')
     BVN = input('what is your BVN? \n')
     Password = input('Type in your unique  four (4) digit password? \n')
     print('        ')  #for clarity
     AccountNumber = AccountNumberGen()
     UserDetails[AccountNumber] = Password 
     print('***************')
     print(AccountNumber)
     print('***************')
     print('Keep it safe!')
     print('You have successfully registered your account!')
     print('            ')  #for clarity
     Login ()

# Login phase
def Login ():
    print('***Login to your account***')
    AccountNumberFromUser = int(input("Type in your account number \n"))
    for AccountNumber, Password in UserDetails.items():
        if AccountNumberFromUser in UserDetails.keys():
            PasswordFromUser = input('Type in your unique for digits password \n')
        if PasswordFromUser == Password:
            print('           ')   #for clarity
            BankingOperations()
        else:
            print('Invalid details, please try again.')
                  
                    
            

# Banking operations
def BankingOperations():
        print ("****%s you have successfully logged into your account!****" % FirstName )
        print('                        ----you currently have 0 balance----')
        SelectBankingOperations = int(input('Select an operation;\n 1. Deposit\n 2. Withdrawal\n 3. Inquiry\n 4. Exit \n'))
        if SelectBankingOperations == 1:
            print('You selected deposit;')
            Deposit()
        elif SelectBankingOperations == 2:
            print('You selected withdrawal;')
            Withdrawal()
        elif SelectBankingOperations == 3:
            print('You selected inquiry;')
            Inquiry()
        elif SelectBankingOperations == 4:
            Exit()
        else:
            print('You have selected an invalid option, try again')



def Deposit():
    print('Feed your account its Good for its health ;)')
    print('                          ') #for clarity
    DepositFunds = int(input('How much will you like to deposit? \n'))
    if DepositFunds > 0:
        global AvailableBalance
        AvailableBalance = 0 + DepositFunds
        print('Your current balance is %s Naira' % AvailableBalance)
        print('Thank you for banking with us!')
        ContinueOrNot()
    else:
        print('Invalid input')


def Withdrawal():
    print('Withdraw on a budget :)')
    print ('                 ') # for clarity
    WithdrawFunds = int(input('How much will you like to withdraw? \n'))
    if WithdrawFunds > 0:
        global CurrentBalance
        CurrentBalance = 0 - WithdrawFunds
        print('Your current balance is %s' % CurrentBalance)
        print('Thank you for banking with us!')
        ContinueOrNot()
    else:
        print('Invalid input')


def Inquiry ():
    print(CurrentBalance)
    print('Thank you for banking with us!')
    ContinueOrNot()

def ContinueOrNot():
    Continued = int(input('Do you want to perform another action?\n 1. Yes \n 2. No \n '))
    if Continued == 1:
        Login()
    elif Continued == 2:
        Exit()
    else:
        print ('Invalid option selected')


def Exit ():
    print('Thank you for banking with us!\n See you next time.ss')

Welcome()


# Logout