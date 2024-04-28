def calc_fixed_monthly_payment(balance, annual_interest_rate):
    '''
    balance: the outstanding balance on the credit card, handles a minimum of 10
    annual_interest_rate: annual interest rate as a float
    
    prints the lowest monthly payment that will pay off all debt in under 1 year
    '''

    monthly_interest_rate = annual_interest_rate / 12.0
    payment = 10
    initial_balance = balance
    
    remaining_balance = balance

    while (remaining_balance > 0):
        for i in range(0, 12):
            monthly_unpaid_balance = remaining_balance - payment
            remaining_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        if (remaining_balance > 0):
            payment += 10
            remaining_balance = initial_balance
    
    print("Lowest Payment: ", round(payment))
    
calc_fixed_monthly_payment(1500, 0.22)
    