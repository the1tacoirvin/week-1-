# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def rollFairDie():
    import random
    x = random.random()
    if x <= 1.0/6:
        return 1
    elif x <= 2.0/6:
        return 2




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(rollFairDie())
