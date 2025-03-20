import json

number=int(input('Enter your favorite number: '))

filename='part1pccexercises/10p11.txt'
with open(filename,'w') as f:
  json.dump(number,f)

with open(filename) as f:
  value=json.load(f)
  print(f'Your favorite number is {value}!')