favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

people=['cindy','jen','sarah','andrea']

for name in people:
  if name in favorite_languages.keys():
    print(f'{name.title()} thanks for responding.')
  else:
    print(f'{name.title()} take the poll!')

#set() used around a list that contains duplicate items, repeated names, set() pulls it out once 
#for language in set(favorite_languages.values()):
# print(language.title())

#ex: languages={'python','ruby','python'}
#output:{'ruby','python'}



