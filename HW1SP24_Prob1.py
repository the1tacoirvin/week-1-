
import random
x = random.random()
def main():
    """this is to find the probalbity of a dice roll after 1000 takes"""
    def rollFairDiesone():
        '''this is to determine how many times one is rolled'''
        one = 0
        x = random.random()
        for i in range(1000):
          if x <= 1.0 / 6:
                one += 1
          return one

    def rollFairDiestwo():
        '''this is to determine how many times two is rolled'''
        two = 0
        x = random.random()
        for i in range(1000):
            if x <= 1.0 / 6:
                two += 1
            return two
    def rollFairDiesthree():
        '''this is to determine how many times three is rolled'''
        three = 0
        x = random.random()
        for i in range(1000):
              if x <= 1.0 / 6:
                    three += 1
              return three
    def rollFairDiesfour():
        '''this is to determine how many times four is rolled'''
        four = 0
        x = random.random()
        for i in range(1000):
              if x <= 1.0 / 6:
                    four += 1
              return four
    def rollFairDiesfive():
        '''this is to determine how many times five is rolled'''
        five = 0
        x = random.random()
        for i in range(1000):
              if x <= 1.0 / 6:
                    five += 1
              return five

    def rollFairDiessix():
        '''this is to determine how many times six is rolled'''
        six = 0
        x = random.random()
        for i in range(1000):
              if x <= 1.0 / 6:
                    six += 1
              return six

    def simulateone(n):
        '''this is to determiny the probliblity of rolling a one'''
        trials = []
        for i in range(n):
            trials.append(rollFairDiesone())
        return(sum(trials)/n)
    def simulatetwo(n):
        '''this is to determiny the probliblity of rolling a two'''
        trials = []
        for i in range(n):
          trials.append(rollFairDiestwo())
        return(sum(trials)/n)

    def simulatethree(n):
        '''this is to determiny the probliblity of rolling a three'''
        trials = []
        for i in range(n):
            trials.append(rollFairDiesthree())
        return(sum(trials)/n)

    def simulatefour(n):
        '''this is to determiny the probliblity of rolling a four'''
        trials = []
        for i in range(n):
            trials.append(rollFairDiesfour())
        return(sum(trials)/n)

    def simulatefive(n):
        '''this is to determiny the probliblity of rolling a five'''
        trials = []
        for i in range(n):
            trials.append(rollFairDiesfive())
        return(sum(trials)/n)
    def simulateSix(n):
        '''this is to determiny the probliblity of rolling a six'''
        trials = []
        for i in range(n):
            trials.append(rollFairDiessix())
        return(sum(trials)/n)

    print("Probability of rolling a 1:",simulateone(1000))
    print("Probability of rolling a 2:",simulatetwo(1000))
    print("Probability of rolling a 3:",simulatethree(1000))
    print("Probability of rolling a 4:",simulatefour(1000))
    print("Probability of rolling a 5:",simulatefive(1000))
    print("Probability of rolling a 6:", simulateSix(1000))

print("After rolling the die 1000 times:")
print(main())

def main2():
    """this is to find the probalbity of a dice roll after 10000 takes"""
    def rollFairDiesone():
        one = 0
        x = random.random()
        for i in range(10000):
              if x <= 1.0 / 6:
                    one += 1
              return one

    def rollFairDiestwo():
        two = 0
        x = random.random()
        for i in range(10000):
              if x <= 1.0 / 6:
                    two += 1
              return two
    def rollFairDiesthree():
        three = 0
        x = random.random()
        for i in range(10000):
              if x <= 1.0 / 6:
                    three += 1
              return three
    def rollFairDiesfour():
        four = 0
        x = random.random()
        for i in range(10000):
              if x <= 1.0 / 6:
                    four += 1
              return four
    def rollFairDiesfive():
        five = 0
        x = random.random()
        for i in range(10000):
              if x <= 1.0 / 6:
                    five += 1
              return five

    def rollFairDiessix():
        six = 0
        x = random.random()
        for i in range(10000):
              if x <= 1.0 / 6:
                    six += 1
              return six

      def simulateone(n):
          '''this is to determiny the probliblity of rolling a one'''
          trials = []
          for i in range(n):
              trials.append(rollFairDiesone())
          return (sum(trials) / n)

      def simulatetwo(n):
          '''this is to determiny the probliblity of rolling a two'''
          trials = []
          for i in range(n):
              trials.append(rollFairDiestwo())
          return (sum(trials) / n)

      def simulatethree(n):
          '''this is to determiny the probliblity of rolling a three'''
          trials = []
          for i in range(n):
              trials.append(rollFairDiesthree())
          return (sum(trials) / n)

      def simulatefour(n):
          '''this is to determiny the probliblity of rolling a four'''
          trials = []
          for i in range(n):
              trials.append(rollFairDiesfour())
          return (sum(trials) / n)

      def simulatefive(n):
          '''this is to determiny the probliblity of rolling a five'''
          trials = []
          for i in range(n):
              trials.append(rollFairDiesfive())
          return (sum(trials) / n)

      def simulateSix(n):
          '''this is to determiny the probliblity of rolling a six'''
          trials = []
          for i in range(n):
              trials.append(rollFairDiessix())
          return (sum(trials) / n)

      print("Probability of rolling a 1:", simulateone(10000))
      print("Probability of rolling a 2:", simulatetwo(10000))
      print("Probability of rolling a 3:", simulatethree(10000))
      print("Probability of rolling a 4:", simulatefour(10000))
      print("Probability of rolling a 5:", simulatefive(10000))
      print("Probability of rolling a 6:", simulateSix(10000))


print("After rolling the die 10000 times:")
print(main2())


def main3():
    def rollUnfairDiesOne():
        one = 0
        x = random.random()
        for i in range(10000):
            if x <= 2.0 / 6:
                one += 1
            return one

    def rollUnfairDiesTwo():
        two = 0
        x = random.random()
        for i in range(10000):
            if x <= 2.0/15:
                two += 1
            return two

    def rollUnfairDiesThree():
        three = 0
        x = random.random()
        for i in range(10000):
            if x <= 2.0/ 15:
                three += 1
            return three

    def rollUnfairDiesFour():
        four = 0
        x = random.random()
        for i in range(10000):
            if x <= 2.0 / 15:
                four += 1
            return four

    def rollUnfairDiesFive():
        five = 0
        x = random.random()
        for i in range(10000):
            if x <= 2.0 / 15:
                five += 1
            return five

    def rollUnfairDiesSix():
        six = 0
        x = random.random()
        for i in range(10000):
            if x <= 2.0 / 15:
                six += 1
            return six

    def simulateone(n):
        '''this is to determiny the probliblity of rolling a one'''
        trials = []
        for i in range(n):
            trials.append(rollUnfairDiesOne())
        return (sum(trials) / n)

    def simulatetwo(n):
        '''this is to determiny the probliblity of rolling a two'''
        trials = []
        for i in range(n):
            trials.append(rollUnfairDiesTwo())
        return (sum(trials) / n)

    def simulatethree(n):
        '''this is to determiny the probliblity of rolling a three'''
        trials = []
        for i in range(n):
            trials.append(rollUnfairDiesThree())
        return (sum(trials) / n)

    def simulatefour(n):
        '''this is to determiny the probliblity of rolling a four'''
        trials = []
        for i in range(n):
            trials.append(rollUnfairDiesFour())
        return (sum(trials) / n)

    def simulatefive(n):
        '''this is to determiny the probliblity of rolling a five'''
        trials = []
        for i in range(n):
            trials.append(rollUnfairDiesFive())
        return (sum(trials) / n)

    def simulateSix(n):
        '''this is to determiny the probliblity of rolling a six'''
        trials = []
        for i in range(n):
            trials.append(rollUnfairDiesSix())
        return (sum(trials) / n)

    print("Probability of rolling a 1:", simulateone(10000))
    print("Probability of rolling a 2:", simulatetwo(10000))
    print("Probability of rolling a 3:", simulatethree(10000))
    print("Probability of rolling a 4:", simulatefour(10000))
    print("Probability of rolling a 5:", simulatefive(10000))
    print("Probability of rolling a 6:", simulateSix(10000))


print("After rolling the die 10000 times:")
print(main3())