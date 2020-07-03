class Collatz:

    def __init__(self, initialInput):
        self.initialNumber = int(initialInput)
        self.numberNowList = []
        self.loopCount = 0
        self.final = None

    def collatz(self):
        """
        initialNumber must be an integer (positive or negative)
        it will loop to either: 1 or the case of negative input largest number in the cycle
        """
        count = 0
        numberNow = self.initialNumber
        largest = self.initialNumber

        while numberNow:
            self.numberNowList.append(int(numberNow))
            if numberNow % 2 != 0:
                numberNow = (3 * numberNow) + 1
            else:
                numberNow = numberNow / 2

            count = count + 1

            if numberNow in [largest, 1]:
                break

            if (largest < numberNow < 0):
                largest = numberNow

        self.loopCount = count
        self.final = int(numberNow)
        self.numberNowList.append(int(numberNow))

    def getInitialNumber(self):
        return self.initialNumber

    def getNumberNowList(self):
        return self.numberNowList

    def getLoopCount(self):
        return self.loopCount

    def getFinalNumber(self):
        return self.final
