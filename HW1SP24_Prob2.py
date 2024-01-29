import random
def main(n):
    ''' find dice roll problitlby for 3 dice as that is all i could figure out'''
    for x in range(10):
        def rollDie():
            '''could not firgue out how to import, so this just decide what number is rolled'''
            import random
            x = random.random()
            if x <= 1.0 / 6:
                return 1
            elif x <= 2.0 / 6:
                return 2
            elif x <= 3.0 / 6:
                return 3
            elif x <= 4.0 / 6:
                return 4
            elif x <= 5.0 / 6:
                return 5
            elif x <= 6.0 / 6:
                return 6
        val = rollDie()

        def rollDices(N):
            ''' finds sum of rolling three times'''
            trials = []
            for i in range(N):
                trials.append(rollDie())
            return sum(trials)
        money = rollDices(3)
        print(money)

    for x in range(1):
        def rollFairDiesone():
            '''is supposed to calcualte problity, does not work'''
            one = 0
            y = random.random()
            for i in range(1000):
                if money == 3:
                    one += 1
                return one

        def rollFairDiestwo():
            '''is supposed to calcualte problity, does not work'''
            two = 0
            y = random.random()
            for i in range(1000):
                if money == 4:
                    two += 1
                return two

        def rollFairDiesthree():
            '''is supposed to calcualte problity, does not work'''
            three = 0
            y = random.random()
            for i in range(1):
                if money == 5:
                    three += 1
                return three

        def rollFairDiesfour():
            '''is supposed to calcualte problity, does not work'''
            four = 0
            x = random.random()
            for i in range(1000):
                if money == 6:
                    four += 1
                return four

        def rollFairDiesfive():
            '''is supposed to calcualte problity, does not work'''
            five = 0
            x = random.random()
            for i in range(1000):
                if money == 7:
                    five += 1
                return five

        def rollFairDiessix():
            '''is supposed to calcualte problity, does not work'''
            six = 0
            x = random.random()
            for i in range(1000):
                if val == 8:
                    six += 1
                return six

        def simulateone(n):
            '''is supposed to calcualte problity, does not work'''
            trials = []
            for i in range(n):
                trials.append(rollFairDiesone())
            return (sum(trials) / n)

        def simulatetwo(n):
            '''is supposed to calcualte problity, does not work'''
            trials = []
            for i in range(n):
                trials.append(rollFairDiestwo())
            return (sum(trials) / n)

        def simulatethree(n):
            '''is supposed to calcualte problity, does not work'''
            trials = []
            for i in range(n):
                trials.append(rollFairDiesthree())
            return (sum(trials) / n)

        def simulatefour(n):
            '''is supposed to calcualte problity, does not work'''
            trials = []
            for i in range(n):
                trials.append(rollFairDiesfour())
            return (sum(trials) / n)

        def simulatefive(n):
            '''is supposed to calcualte problity, does not work'''
            trials = []
            for i in range(n):
                trials.append(rollFairDiesfive())
            return (sum(trials) / n)
        def simulatesix(n):
            '''is supposed to calcualte problity, does not work'''
            trials = []
            for i in range(n):
                trials.append(rollFairDiessix())
            return (sum(trials) / n)

        print("Probability of rolling a 1:", simulateone(10))
        print("Probability of rolling a 2:", simulatetwo(10))
        print("Probability of rolling a 3:", simulatethree(10))
        print("Probability of rolling a 4:", simulatefour(10))
        print("Probability of rolling a 5:", simulatefive(10))
        print("Probability of rolling a 6:", simulatesix(10))

print(main(10))