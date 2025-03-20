wanted_places=['france','brazil','colombia','russia','italy']
print(wanted_places)
print(sorted(wanted_places))    #sorted function-sorted alphabetically temporarily, so doesn't change list
print(wanted_places)
wanted_places.reverse()    #method, permanently reverses list
print(wanted_places)
wanted_places.reverse()     #reverse again so goes back to original list
print(wanted_places)
wanted_places.sort()        #method, permanently sorts alphabetically list
print(wanted_places)
wanted_places.sort(reverse=True)    #method, permanently sorts alphabetically in reverse list
print(wanted_places)

length=len(wanted_places)
print(length)

