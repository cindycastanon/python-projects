
invites= ['neymar', 'beckham', 'messi', 'pele', 'cristiano', 'iniesta']
print("We're so sorry! We can only invite two people!")
removed=invites.pop()
print(f"{removed.title()}, we're so sorry we can't invite you to dinner!")
removed=invites.pop()
print(f"{removed.title()}, we're so sorry we can't invite you to dinner!")
removed=invites.pop()
print(f"{removed.title()}, we're so sorry we can't invite you to dinner!")
removed=invites.pop()
print(f"{removed.title()}, we're so sorry we can't invite you to dinner!")

print(f'{invites[0].title()}, you are still invited to dinner!')
print(f'{invites[1].title()}, you are still invited to dinner!')

del invites[0]
print(invites)
invites.remove('beckham')
print(invites)