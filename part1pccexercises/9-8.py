class User:
  def __init__(self,first_name,last_name, age, weight,location):
    self.first=first_name.title()
    self.last=last_name.title()
    self.age=age
    self.weight=weight
    self.location=location.title()
  
  def describe_user(self):
    print(f"Here is the user's information:\nFirst name:{self.first}\nLast Name:{self.last}\nAge:{self.age}\nWeight:{self.weight}\nLocation:{self.location}")

  def greet_user(self):
    print(f'Hello {self.first} {self.last}!')



class Admin(User):
  def __init__(self,first_name,last_name, age, weight,location):
    super().__init__(first_name,last_name, age, weight,location)
    self.privileges=Privileges()
    

  def show_privileges(self):
    for p in self.privileges:
      print(f'- {p}')

class Privileges:
  def __init__(self, privileges=[]):
    self.privileges=privileges

  def show_privileges(self):
    print(f'Privileges:')
    if self.privileges:
      for privilege in self.privileges:
        print(f"- {privilege}")
    else:
      print("- This user has no privileges.")

admin=Admin('Cindy','Castanon','19','135','Florida')
admin.describe_user()

admin.privileges.show_privileges()

print("\nAdding privileges...")
admin_privileges=['can add post','can delete post','can ban user']

admin.privileges.privileges=admin_privileges

admin.privileges.show_privileges()

