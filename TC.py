
class Person():
    def __init__(self):
        self.name = str(input("Enter a name: "))
        self.total = int(input("Enter their total: "))
        self.share = 0

def getPeople(x):
    totalP = int(input("Enter many people are eating: "))
    i = 0
    for i in range(totalP):
        x.append(Person())

def getTotal(x):
    n = 0
    for i in range(len(x)):
        n += x[i-1].total
    return n

def getShares(x, y):
    for i in range(len(x)):
        x[i-1].share = (x[i-1].total / y) * 100

def getDiscount():
    answer = str(input("Was there a discount applied (y/n): "))
    if answer == "n":
        return False
    elif answer == "y":
        return True


def main():
    plist = list()
    getPeople(plist)

    takeawayTotal = getTotal(plist)
    getShares(plist, takeawayTotal)
    takeawayCost = int(input("Enter the final amount payed: "))

    discount = getDiscount()

    for i in range(len(plist)):
        print(plist[i-1].name, plist[i-1].share)



main()
