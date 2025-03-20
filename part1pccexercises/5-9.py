#Add an if test to 5-8 to make sure the list of users is not empty. If the list is empty, print the message We need to find some users! Remove all of the usernames from your list, and make sure the correct message is printed.

usernames=[]
if usernames:
  for username in usernames:
      print(f'Hello {username}, would you like to see a status report?')
else:
  print(f'We need more users!')
  
