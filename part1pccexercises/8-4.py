#default value- always include it at the end

#example 1
def make_shirt(message, size='large'):
  print(f"The size of the shirt is {size} and the message on the shirt will be '{message}'.")

make_shirt('I love python')



#example 2
def make_shirt(size, message='I love python'):
  print(f"The size of the shirt is {size} and the message on the shirt will be '{message}'.")

make_shirt('large')

