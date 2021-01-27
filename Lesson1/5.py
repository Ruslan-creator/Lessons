revenue = int(input('Enter your revenue: '))
costs = int(input('Enter your costs: '))
if revenue >= costs:
    profitability = revenue/costs
    print(f'You have {profitability} profitability')
    nun_empl= int(input('How many people do you have?: '))
    profit_for_1 = (revenue-costs)/nun_empl
    print(f'Profit for 1 person = {profit_for_1}')
else:
    print('You have not profit,sorry')
