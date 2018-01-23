import random

f_names = ['Nicholas', 'Alexander', 'Charles', 'Mechele', 'Elaine', 'Harry']
l_names = ['Vilela', 'Bayley', 'Mosch', 'Cline']
colors = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']
activities = ['playing games', 'programming', 'hunting', 'football']
age = range(2,80)


print('Your name is %s %s, you are %s years old.' % (random.choice(f_names), random.choice(l_names), random.choice(age)))
print('Your favorite color is %s, and your favorite activity is %s' % (random.choice(colors), random.choice(activities)))
