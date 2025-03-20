pet1={'type':'dog', 'owner':'cindy'}
pet2={'type':'cat', 'owner':'jason'}
pet3={'type':'pig', 'owner':'ana'}
pet4={'type':'goat', 'owner':'joe'}

pets=[pet1, pet2, pet3, pet4]
for pet in pets:
  type=f'{pet['type']}'
  owner=f'{pet['owner']}'
  print(f"The pet type is: \n{type}\nThe owner's name is:\n{owner.title()}\n ")
