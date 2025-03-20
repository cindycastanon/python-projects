current_users=['snip24','Cindy19','butterfly','princess_','michelle05']
new_users=['jess34','cindy19','jason045','princess_','lopez05']
copied_list=[value.lower() for value in current_users]
for value in new_users:
  if value.lower() in copied_list:
    print('Person will need to enter a username.')
  else:
    print('Username is available.')



