import random
x = random.random()
def main():
      def rollFairDiesone():
            one = 0
            x = random.random()
            for i in range(1000):
                  if x <= 1.0 / 6:
                        one += 1
                  return one

      def rollFairDiestwo():
            two = 0
            x = random.random()
            for i in range(1000):
                  if x <= 1.0 / 6:
                        two += 1
                  return two
      def rollFairDiesthree():
            three = 0
            x = random.random()
            for i in range(1000):
                  if x <= 1.0 / 6:
                        three += 1
                  return three
      def rollFairDiesfour():
            four = 0
            x = random.random()
            for i in range(1000):
                  if x <= 1.0 / 6:
                        four += 1
                  return four
      def rollFairDiesfive():
            five = 0
            x = random.random()
            for i in range(1000):
                  if x <= 1.0 / 6:
                        five += 1
                  return five

      def rollFairDiessix():
            six = 0
            x = random.random()
            for i in range(1000):
                  if x <= 1.0 / 6:
                        six += 1
                  return six

      def simulateone(n):
          trials = []
          for i in range(n):
              trials.append(rollFairDiesone())
          return(sum(trials)/n)
      def simulatetwo(n):
          trials = []
          for i in range(n):
              trials.append(rollFairDiestwo())
          return(sum(trials)/n)

      def simulatethree(n):
          trials = []
          for i in range(n):
              trials.append(rollFairDiesthree())
          return(sum(trials)/n)

      def simulatefour(n):
          trials = []
          for i in range(n):
              trials.append(rollFairDiesfour())
          return(sum(trials)/n)

      def simulatefive(n):
          trials = []
          for i in range(n):
              trials.append(rollFairDiesfive())
          return(sum(trials)/n)

      print("Probability of rolling a 1:",simulateone(1000))
      print("Probability of rolling a 2:",simulatetwo(1000))
      print("Probability of rolling a 3:",simulatethree(1000))
      print("Probability of rolling a 4:",simulatefour(1000))
      print("Probability of rolling a 5:",simulatefive(1000))
print("After rolling the die 1000 times:")
print(main())