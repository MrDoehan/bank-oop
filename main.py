print("Initialisation for your main bank account (keep in mind you also have a secondary savings account")
starter = input("How much money would you like to initially put in? ")
form = input("What type of bank account is it? ")
user = input("Who is the owner? ")
class bank:
  def __init__ (self, amount, type, owner):
    self.amount = amount
    self.type = form
    self.owner = user
 
  def withdraw(self):
    value = int(input("How much would you like to withdraw? "))
    self.amount = int(self.amount) - value

  def show(self):
    print(f"Balance: {self.amount}")
    print(f"Name of owner: {self.owner}")
    print(f"Type of account: {self.type}")
    
  def deposit(self):
    val = int(input("How much would you like to put in? "))
    self.amount = int(self.amount) + val
  
  def change(self):
    newed = input("Who is the new owner of the account? ")
    self.owner = newed
  
  def transfer(self):
    pass
  
  def outer(self, va):
    self.amount = int(self.amount) - va
  
  def idk(self, value):
    self.amount = int(self.amount) + value

class alt:
  
  def __init__ (self, amount, type):
    self.amount = 0
    self.type = "savings"
  
  def take(self):
    thing = int(input("How much money would you like to take out? "))
    
    while int(self.amount) - thing < 0:
      print("You cant do that because no")
      thing = int(input("How much money would you like to take out? "))
    self.amount = self.amount - thing
    first.idk(thing)
  
  def transfer(self):
    send = int(input("How much money would you like to take out? "))
    self.amount = int(self.amount) + send
    first.outer(send)

  def show(self):
    print("Secondary savings bank account")
    print(f"Balance: {self.amount}")
    print(f"Type of account{self.type}")


first = bank(starter, form, user)
first.show()
action = input("What would you like to do? show/withdraw/deposit/change/send to alt/take from alt/show alt ")
secondary = alt(0, "savings")

while action != "":
  if action == "show":
    first.show()
  if action == "withdraw":
    first.withdraw()
  if action == "deposit":
    first.deposit()
  if action == "change":
    first.change()
  if action == "send to alt":
    secondary.transfer()
  if action == "take from alt":
    secondary.take()
  if action == "show alt":
    print("This is your savings bank account")
    secondary.show()
  action = input("What would you like to do? show/withdraw/deposit/change/send to alt/take from alt/show alt ")
  
  
