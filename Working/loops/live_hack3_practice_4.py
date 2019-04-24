
print("Welcome to the compound interest calculator")

# get theinvestment amount, interest rate and time of investment
yearly_invest = int(input("\nEnter the yearly investment: "))
interest_rate = float(input("Enter the interest rate: "))
invest_time = int(input("Enter the number of years for the investment (up to 15 years): "))
while invest_time < 1 or invest_time > 15:
    print("Invalid")
    invest_time = int(input("Enter the number of years for the investment (up to 15 years): "))

# set the current total and amount in account
total = 0
amount_in_account = 0

# create table labels
print("{0:>10} {1:>20} {2:>17} {3:>10}".format("Year", "Amount in Account", "Interest Earned", "Total"))


# loop through and compute values for each year, creating a table
for i in range(1, invest_time+1):

    # set the year and amount in account
    year = i
    amount_in_account = total + yearly_invest

    # compute interest
    interest_earned = amount_in_account * (interest_rate/100)

    # refresh total variable
    total = interest_earned + amount_in_account

    print("{0:>10} {1:>20.2f} {2:>17.2f} {3:>10.2f}".format(year, amount_in_account, interest_earned, total))