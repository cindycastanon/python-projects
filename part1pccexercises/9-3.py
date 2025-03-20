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

user1=User('Cindy','Castanon','19','135','Florida')
user1.describe_user()
user1.greet_user()

user2=User('James','Williams','50','150','New York')
user2.describe_user()
user2.greet_user()

user3=User('Fernanda','Ramirez','31','145','Texas')
user3.describe_user()
user3.greet_user()