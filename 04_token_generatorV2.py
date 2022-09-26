import random

# main route goes here
tokens = ["unicorn", "horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

# Testing loop to generate 20 token
for item in range (0,500):
     chosen = random.choice(tokens)

     #Adjust balance
     if chosen == "unicorn":
       balance += 4

       #Adjust balance
     if chosen == "donkey":
       balance -= 1

     else:
         balance -= 0.5


print ()
print("Starting Balance: ${: .2f}".format(STARTING_BALANCE))
print("Final Balance: ${: .2f}".format(balance))
