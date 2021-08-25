# ATM_SYSTEM_Controller
- Pre_Dev_ATM_Controller_SW

# Description
This SW is designed to provide the ATM service to the customer.
The service is summarized below:
- Confirm the balance
- Deposit
- Withdraw

# Dev. Environment
- ATM Controller (main.py)
- ATM HW (ATM_HW.py)
- Network to Bank account system (ATM_Bank.py)

# Files
- main.py: ATM controller base SW

# Logic Flow
The logic is summarized below:
- To confirm the insertion of debit card (To be integrated with ATM HW)
- To confirm the PIN No (To be integrated with the bank account check system)
- To select ATM sevice: See balance, deposit, withdraw (To update the balance by connecting the bank account)

# Test
- Validation of Pin NO
- Confirmation of each ATM service on the basis of the input requested
- The calculation of the final balance after completion of the transaction
