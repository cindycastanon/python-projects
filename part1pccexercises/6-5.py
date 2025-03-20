river_info={'nile':'egypt', 'amazon':'peru','volga':'russia'}
for name, country in river_info.items():
  print(f'{name.title()} runs through {country.title()}.')

for name in river_info.keys():
  print(f'{name.title()}')

for country in river_info.values():
  print(f'{country.title()}')