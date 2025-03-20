person_info1={'first name':'Cindy','last name': 'Castanon','age':'19','city':'Tampa'}
person_info2={'first name':'ana','last name': 'suazo','age':'18','city':'Houston'}
person_info3={'first name':'luis','last name': 'lopez','age':'30','city':'New york'}
people=[person_info1, person_info2, person_info3]
for person in people:
  name = f"{person['first_name'].title()} {person['last_name'].title()}"
  age = person['age']
  city = person['city'].title()
    
  print(f"{name}, of {city}, is {age} years old.")