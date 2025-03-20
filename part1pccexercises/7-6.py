#Use a conditional test in the while statement to stop the loop.

while True:
  message=input("Enter toppings until 'quit' is entered.")
  if message != 'quit':
    print(f"I'll add {message} to your pizza.")
  else:
    break


#Use an active variable to control how long the loop runs.
active=True
while active:
  message=input("Enter toppings until 'quit' is entered.")
  if message == 'quit':
    active=False
    
  else:
    print(f"I'll add {message} to your pizza.")



#Use a break statement to exit the loop when the user enters a 'quit' value.
while True:
  message=input("Enter toppings until 'quit' is entered.")
  if message != 'quit':
    print(f"I'll add {message} to your pizza.")
  else:
    break
