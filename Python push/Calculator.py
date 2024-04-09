print("Welcome to our FinTech company")

principal_amount = float(input("Enter the principal amount \n"))

interest_rate = float(input("Enter the annual interest rate\n"))

loan_duration = float(input("Enter the duration in years\n"))


total_amount = principal_amount * interest_rate * loan_duration



print("the monthly payment is ", str(total_amount))