def calc_fixed_monthly_payment_bisect(balance, annual_interest_rate):
    '''
    balance: the outstanding balance on the credit card
    annual_interest_rate: annual interest rate as a float
    
    prints the lowest monthly payment that will pay off all debt in under 1 year
    uses bisection serach to find the lowest payment possible
    '''
    monthly_interest_rate = annual_interest_rate / 12.0
    
    lower_bound = balance / 12.0
    upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0

    payment = (lower_bound + upper_bound) / 2

    remaining_balance = balance

    while (remaining_balance > 0.01):
        for i in range(0, 12):
            monthly_unpaid_balance = remaining_balance - payment
            remaining_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
            
        if abs(remaining_balance) < 0.01:
            break

        if (remaining_balance < 0):
            upper_bound = payment
            payment = (lower_bound + upper_bound) / 2
        else:
            lower_bound = payment
            payment = (lower_bound + upper_bound) / 2
        remaining_balance = balance
    
    print("Lowest Payment: ", round(payment, 2))
    
calc_fixed_monthly_payment_bisect(320000, 0.2) #29157.09