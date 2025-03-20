

dict1={}
active=True
while active:
  name=input('What is your name:')
  place=input('If you could visit one place in the world, where would you go?')
  dict1[name]=place
  repeat=input('Would you like to let another person respond? (yes/no) ')
  if repeat=='no':
    active=False            #do the active at the end of while loop
print('\nResults are:  ')
for key, value in dict1.items():
  print(f'{key.title()} wants to go to {value.title()}')
