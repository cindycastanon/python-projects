def location(city,country):
  result=f'{city.title()}, {country.title()}'
  return result


print("Enter 'quit' when done.")
while True:
  city=input('Enter a city name: ')
  if city.lower()=='quit':
    break
  country=input('Enter country name: ')
  if country.lower() =='quit':
    break
  result=location('Tampa','US')
  print(result)