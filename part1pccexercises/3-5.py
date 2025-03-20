# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting Print a second set of invitation messages, one for each person who is still in your list.
invites = ['messi', 'pele', 'cristiano']
print(f"{invites[0].title()} can't make it to the dinner.")
del invites[0]   #we can never assign a variable to this, not possible
print(invites)
invites.insert(0,'neymar')      #for replacing, can't assign variable either

print(f'{invites[0].title()}, you are invited to dinner!')
print(f'{invites[1].title()}, you are invited to dinner!')
print(f'{invites[2].title()}, you are invited to dinner!')