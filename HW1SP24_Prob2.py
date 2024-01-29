import random
def main(n):
    for x in range(10):
        def rollDie():
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
            trials = []
            for i in range(N):
                trials.append(rollDie())
            return sum(trials)
        money = rollDices(3)
        print(money)

    for x in range(1):
        def rollFairDiesone():
            one = 0
            y = random.random()
            for i in range(1000):
                if money == 3:
                    one += 1
                return one

        def rollFairDiestwo():
            two = 0
            y = random.random()
            for i in range(1000):
                if money == 4:
                    two += 1
                return two

        def rollFairDiesthree():
            three = 0
            y = random.random()
            for i in range(1):
                if money == 5:
                    three += 1
                return three

        def rollFairDiesfour():
            four = 0
            x = random.random()
            for i in range(1000):
                if money == 6:
                    four += 1
                return four

        def rollFairDiesfive():
            five = 0
            x = random.random()
            for i in range(1000):
                if money == 7:
                    five += 1
                return five

        def rollFairDiessix():
            six = 0
            x = random.random()
            for i in range(1000):
                if val == 8:
                    six += 1
                return six

        def simulateone(n):
            trials = []
            for i in range(n):
                trials.append(rollFairDiesone())
            return (sum(trials) / n)

        def simulatetwo(n):
            trials = []
            for i in range(n):
                trials.append(rollFairDiestwo())
            return (sum(trials) / n)

        def simulatethree(n):
            trials = []
            for i in range(n):
                trials.append(rollFairDiesthree())
            return (sum(trials) / n)

        def simulatefour(n):
            trials = []
            for i in range(n):
                trials.append(rollFairDiesfour())
            return (sum(trials) / n)

        def simulatefive(n):
            trials = []
            for i in range(n):
                trials.append(rollFairDiesfive())
            return (sum(trials) / n)
        def simulatesix(n):
            trials = []
            for i in range(n):
                trials.append(rollFairDiessix())
            return (sum(trials) / n)

        print("Probability of rolling a 1:", simulateone(10))
        print("Probability of rolling a 2:", simulatetwo(10))
        print("Probability of rolling a 3:", simulatethree(10))
        print("Probability of rolling a 4:", simulatefour(10))
        print("Probability of rolling a 5:", simulatefive(10))

print(main(10))