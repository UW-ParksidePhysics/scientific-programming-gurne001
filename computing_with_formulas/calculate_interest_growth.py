initial_amount = 1000 #dollars
interest_rate = 4.72 #percent yearly, us govt security as of 2/14/2024
years = 3

total = initial_amount * (1 + interest_rate / 100) ** years
growth = total - initial_amount

print(f'Initial amount: ${initial_amount:,.2f}')
print(f'Interest rate: {interest_rate:,.2f}%')
print(f'Growth: ${growth:,.2f}')