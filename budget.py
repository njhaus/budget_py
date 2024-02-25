from functools import reduce

class Category:
  def __init__(self, name, allotted = 0, balance = 0):
    self.ledger = []
    self.balance = balance
    self.name = name
    self.allotted = allotted

  @property
  def spent(self):
      amount = self.allotted - self.balance
      return amount if amount > 0 else 0 
  
  def __str__(self):
    # Create a line of exactly 30 characters with the name in the middle for title line:
    stars = int((30 - len(self.name)) / 2)
    title_line = "*" * stars + self.name
    title_line += "*" * stars + '\n' if stars * 2 + len(self.name) == 30 else "*" * (stars + 1) + '\n'
    # total line:
    total_line = f"Total: {str(self.balance)}"
    # concat a formatted string for each item in the ledger:
    transaction_printout = ''
    for transaction in self.ledger:
      t_desc = transaction["description"] if len(transaction["description"]) <= 23 else transaction["description"][0:23]
      transaction_printout += "{:<23}{:>7.2f}\n".format(t_desc, transaction["amount"])
    return title_line + transaction_printout + total_line
  
  def deposit(self, amount, description = ''):
    new_deposit = {"amount": amount, "description": description}
    self.balance += amount
    self.ledger.append(new_deposit)
    print(f'Deposit of {amount} in {self.name} successful!')

  def withdraw(self, amount, description = ''):
    if not self.check_funds(amount):
      print(f'You do not have enough funds to complete this withdraw transaction. (Attempted to withdraw ${amount} from {self.name}, current funds: ${self.balance})\n')
      return False
    else:
      new_withdrawl = {"amount": amount * -1, "description": description}
      self.balance -= amount
      self.ledger.append(new_withdrawl)
      print(f'Withdrawal of {amount} from {self.name} successful!')
      return True
    
  def get_balance(self):
    print(f"BALANCE: {self.balance}\n")
    return self.balance
  
  def set_name(self, new_name):
    self.name = new_name

  def set_allotted(self, new_alloted):
    self.allotted = new_alloted
  
  def reset_ledger(self):
    self.ledger = []
    self.balance = self.allotted

  def transfer(self, amount, category):
    if not self.check_funds(amount):
      print(f'You do not have enough funds to complete this transfer transaction. (Attempted to withdraw ${amount} from {self.name}, current funds: ${self.balance})\n')
      return False
    # Category is saved as a property in a class itself within the test module (i.e. self.category_name), so can be accessed simply by the variable 'category'. In workable app, will need to acces categories[category] to vaerify existence
    elif category is None:
      print('The category selected for this transfer does not exist.\n')
      return False
    else:
      new_transfer = {"amount": amount * -1, "description": f"Transfer to {category.name}"}
      self.balance -= amount
      self.ledger.append(new_transfer)
      # Will need to access the category object in workable app (category = categories[category])
      category.deposit(amount, f"Transfer from {self.name}")
      print(f"SUCCESS transferring ${amount} from {self.name} to {category.name}\n")
      return True

  def check_funds(self, amount):
    return True if self.balance >= amount else False


def create_spend_chart(categories):
  percentages = range(100, -1, -10)
  chart = 'Percentage spent by category\n'
  spent_per_category = list(map(lambda c: c.spent, categories))
  total_spent = reduce(lambda x, y: x + y, spent_per_category)
  if total_spent == 0:
    return 'You have not spent money in any category!'
  category_percentages = list(map(lambda c: round((c / total_spent * 100), 2), spent_per_category))
  category_names = list(map(lambda c: c.name, categories))
  for pct in percentages:
    line = '{:>3}| '.format(pct)
    for c in category_percentages:
      if c >= pct:
        line += 'o  '
      else:
        line += ' ' * 3
    line += '\n'    
    chart += line
  chart += '    ----------\n'
  for i in range(len(max(category_names, key = len))):
    chart += ' ' * 5
    for c in category_names:
      try:
        chart += f'{c[i]}  '
      except IndexError:
        chart += ' ' * 3
    chart += '\n' if i != len(max(category_names, key = len)) - 1 else ''
  return chart