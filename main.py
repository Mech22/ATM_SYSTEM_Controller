# ATM Controller

import ATM_HW
import ATM_Bank

pin_no = 0
pin_try = 3
ser_try = 1
ser_no = 0

print("\tWelcome to PYTHON ATM\nInsert Your Debit Card\n")

if(ATM_HW.deb_cd_valid() == True):

    while (pin_try != 0):

        print("Enter your pin number: ")
        pin_no = int(input())

        if(ATM_Bank.pin_no_valid(pin_no)):
            break

        else:
            print("Wrong number")
            pin_try -= 1

            if(ATM_Bank.pin_try == 0):
                print("Please confirm your pin number with the Bank again")


    while(ATM_Bank.pin_no_valid(pin_no) and ser_try == 1):
        print("\n1.See balance\n2.Deposit\n3.Withdraw\nSelect a service number:")
        ser_no = int(input())

        if(ser_no == 1):
            money = ATM_Bank.amt_mon_account()
            print("Your bank account: $%d" % money)
            ser_try -= 1
            pass

        elif(ser_no == 2):
            print("\nPlease insert money to deposit:")
            dept_money = int(input())
            money = ATM_Bank.amt_mon_account()
            money += dept_money
            if (ATM_Bank.conn_bank_sys(money) == True):
                print("Transaction completed")
                print("Your bank account: $%d" %money)
            else:
                print("Technical problem occurs\nTransaction not completed")
            ser_try -= 1

        elif(ser_no == 3):
            money = ATM_Bank.amt_mon_account()
            print("\nPlease insert money to withdraw (Maximum: $%d):" %money)
            wthrl_money = int(input())
            money -= wthrl_money
            if (ATM_Bank.conn_bank_sys(money) == True):
                print("Transaction completed")
                print("Your bank account: $%d" %money)
            else:
                print("Technical problem occurs\nTransaction not completed")
            ser_try -= 1

        else:
            print("Not applicable service number!")

    print("\nPlease Take your debit card.\nThank you for your service!")