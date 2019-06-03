annual_salary = int(input("Type annual salary here:"))
portion_saved = float(input("Type the portion you want to save (as a decimal):"))
total_cost = float(input("Type the cost of your dream house here:"))

monthly_salary = (annual_salary / 12.0)
down_payment = .25 * total_cost
current_savings = 0
r = 0.04
monthly_savings = ((annual_salary/12)*portion_saved) + current_savings*r/12

months = 0
#We want to exit the loop when there is enough savings for the down payment
while (current_savings <= down_payment):
    monthly_savings = ((annual_salary/12)*portion_saved) + current_savings*r/12
    current_savings = current_savings+monthly_savings
    months = months + 1
print("It will take {} months to save!" .format(months))
