class User:
  def __init__(self,first_name,last_name, age, weight,location):
    self.first=first_name.title()
    self.last=last_name.title()
    self.age=age
    self.weight=weight
    self.location=location.title()
    self.login_attempts=0
    
  
  def describe_user(self):
    print(f"Here is the user's information:\nFirst name:{self.first}\nLast Name:{self.last}\nAge:{self.age}\nWeight:{self.weight}\nLocation:{self.location}")

  def greet_user(self):
    print(f'Hello {self.first} {self.last}!')

  def increment_login_attempts(self):
    self.login_attempts+=1

  def reset_login_attempts(self):
    self.login_attempts=0


user1=User('Cindy','Castanon','19','135','Florida')
user1.describe_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f'Login attempts: {user1.login_attempts}')

print("Resetting login attempts...")
user1.reset_login_attempts()
print(f"  Login attempts: {user1.login_attempts}")
