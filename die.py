# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def rollFairDie():
    '''this function will roll fair dice rolls, unsure if  this works but it gives number'''
    import random
    x = random.random()
    one = 0
    two= 0
    three = 0
    four = 0
    five = 0
    six = 0
    if x <= 2.0/6:
        return 1
    elif x <= 2.0/6:
        return 2
    elif x <= 3.0/6:
        return 3
    elif x <= 4.0/6:
        return 4
    elif x <= 5.0/6:
        return 5
    elif x <= 6.0/6:
        return 6
print(rollFairDie())