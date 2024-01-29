import random
import testdie
x = random.random()

RFD=testdie
def main():
    for i in range(1000)

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

    print("Probability of rolling a 1:", simulateone(1000))
    print("Probability of rolling a 2:", simulatetwo(1000))
    print("Probability of rolling a 3:", simulatethree(1000))
    print("Probability of rolling a 4:", simulatefour(1000))
    print("Probability of rolling a 5:", simulatefive(1000))


print("After rolling the die 1000 times:")
print(main())