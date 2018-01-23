import random

def numbers():
    print('This a random dice roller for any number.')
    rolls = int(input('Enter the number of rolls: '))
    minimum = int(input('Enter a min number: '))
    maximum = int(input('Enter a max number: '))

    roll_l = []
    for _ in range(rolls):
        roll = random.randint(minimum, maximum)
        roll_l.append(roll)
        print('Rolled:', roll)

    print('Average:', sum(roll_l) / len(roll_l))

numbers()
