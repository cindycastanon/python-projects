prompt='How old are you? '

while True:
  message=input(prompt)
  age=input(message)
  if message == 'quit':
    break
  if age<3:
    print('Your ticket is free! ')
  elif 3<age<12:
    print('Your ticket is $10.')
  else:
    print('Your ticket is $15.')
