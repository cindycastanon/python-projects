cities={'tampa':
        {'country':'US', 'population':'230000','fact':'very hot'}, 'paris':{'country':'France', 'population':'4500000','fact':'has a big tower'}, 'venice':{'country':'italy', 'population': '6790000', 'fact': 'famous for pretty lake'}}
for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The fact is: {fact} ")