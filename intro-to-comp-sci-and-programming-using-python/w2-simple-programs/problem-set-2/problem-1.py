def calculate_cred_balance(
        balance,
        annual_interest_rate,
        minimum_monthly_payment_rate):
    '''
    balance: the outstanding balance on the credit card
    annual_interest_rate: annual interest rate as a float
    minimum_monthly_payment_rate: minimum monthly payment rate as a float

    prints the remaining balance at the end of 12 months
    '''
    
    monthly_interest_rate = annual_interest_rate / 12.0
    remaining_balance = balance

    for i in range(0, 12):
        minimum_monthly_payment = minimum_monthly_payment_rate * remaining_balance
        monthly_unpaid_balance = remaining_balance - minimum_monthly_payment
        remaining_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    
    print("Remaining balance: ", round(remaining_balance, 2))
    
balance = 484
annual_interest_rate = 0.2
minimum_monthly_payment_rate = 0.04

calculate_cred_balance(balance, annual_interest_rate, minimum_monthly_payment_rate)