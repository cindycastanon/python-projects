#You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table. Use insert() to add one new guest to the beginning of your list. Use insert() to add one new guest to the middle of your list. Use append() to add one new guest to the end of your list. Print a new set of invitation messages, one for each person in your list.
invites = ['messi', 'pele', 'cristiano']

print(f'Great news! We found a bigger dinner table!')
invites.insert(0,'neymar')        #(index, value) 
invites.insert(1,'beckham')       #(index, value)
invites.append('iniesta')         #ADDS TO END OF LIST
print(invites)

print(f'{invites[0].title()}, you are invited to dinner!')
print(f'{invites[1].title()}, you are invited to dinner!')
print(f'{invites[2].title()}, you are invited to dinner!')
print(f'{invites[3].title()}, you are invited to dinner!')
print(f'{invites[4].title()}, you are invited to dinner!')
print(f'{invites[5].title()}, you are invited to dinner!')
