

filenames=['/Users/cindycastanon/python-projects/part1pccexercises/10p8dogs.txt','/Users/cindycastanon/python-projects/part1pccexercises/10p8cats.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")