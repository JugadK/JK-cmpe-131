def calculate_apr(principle, interest_rate, years):
    """
Calculates the total amount of money made given an interest rate, years, and principle

Parameters
----------
principle: float
    The original amount of money in the account

interest_rate: float
    The interest rate for the account

years: int
    The total amount of years that should be used in the calculation

Returns
--------
float

Examples
---------
calculate_apr(500.0,0.03,65)
3414.99136729
calculate_apr(534.0,0.07,65)
43399.7079046
    """
    if(not isinstance(principle,float)):
        return False
    if(not isinstance(interest_rate,float)):
        return False
    if(not isinstance(years,int)):
        return False
    
    number = 0
    while(number < years):
        principle = principle*(1+interest_rate)
        number= number+1
    return principle



print(calculate_apr(500.0,0.03,65))
print(calculate_apr(534.0,0.07,65))
print(calculate_apr('afdsf',0.03,65))
