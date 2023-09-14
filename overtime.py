# Prompt the user for hours and rate per hour
hours_str = input('Enter hours worked: ')
rate_str = input('Enter hourly rate: ')

try:
    hours = float(hours_str)
    rate = float(rate_str)
except ValueError:
    print('Please enter valid numerical values for hours and rate.')
    exit()

if hours <= 40:
    gross_pay = hours * rate
else:
    regular_hours = 40
    overtime_hours = hours - 40
    overtime_rate = 1.5 * rate
    gross_pay = (regular_hours * rate) + (overtime_hours * overtime_rate)

print('Gross Pay:', gross_pay)