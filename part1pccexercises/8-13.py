#Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

def build_profile(first_name, last_name, **more_info):
  more_info['first']=first_name
  more_info['last']= last_name
  return more_info

result=build_profile('Cindy','Castanon', age='19', weight='135 lb', height="5'4")
print(result)

