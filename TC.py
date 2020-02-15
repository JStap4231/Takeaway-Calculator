
class Person():
    def __init__(self):
        self.name = str(input("Enter a name: "))
        self.total = int(input("Enter their total: "))
        self.share = 0
        self.amount_owed = 0

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
        x[i-1].share = (x[i-1].total / y)

def getDiscount():
    answer = str(input("Was there a discount applied (y/n): "))
    if answer == "n":
        return False
    elif answer == "y":
        return True

def getTotal_owed(x, y):
    for i in range(len(y)):
        y[i-1].amount_owed = x * y[i-1].share

def main():
    plist = list()
    getPeople(plist)

    takeawayTotal = getTotal(plist)
    getShares(plist, takeawayTotal)
    takeawayCost = int(input("Enter the final amount paid: "))

    discount = getDiscount()

    if discount == True:
        getTotal_owed(takeawayCost, plist)
    elif dicount == False:
        getTotal_owed(takeawayTotal, plist)

    print("The final totals to pay are:")
    for i in range(len(plist)):
        print(plist[i-1].name, " owes £", plist[i-1].amount_owed, ".")



main()
