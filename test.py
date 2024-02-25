# This entrypoint file to be used in development. 
import budget
from budget import create_spend_chart
from unittest import main
from test_module import UnitTests

print("RUNNING TESTS! If 'OK' is printed at the end, all tests have passed.")
food = budget.Category("Food", 1000)
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing", 50)
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto", 1000)
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)