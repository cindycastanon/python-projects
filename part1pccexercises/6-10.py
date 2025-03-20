favorite_numbers = {
    'mandy': ['42','20','18'],
    'micah': ['23','67','89'],
    'gus': ['102','879','73'],
    'hank': ['1000_000','39','378'],
    'maggie': ['46','498','231']
    }

for name, number in favorite_numbers.items():
  print(f'Favorite numbers of {name.title()} are:')
  for num in number:
    print(f'{num}')