# day 11

# https://adventofcode.com/2022/day/11


# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1


class Monkey():
    def __init__(self, number, items, operation, value, dividableBy, throwTrue, throwFalse) -> None:
        self.no = number
        self.items = items
        self.op = operation # '+' , '*' /
        self.val = value # None if old value should be used
        self.div = dividableBy
        self.ifTrue = throwTrue
        self.ifFalse = throwFalse
        self.count = 0

    def __str__(self):
        return f"m:{self.no}, {self.items}, count:{self.count}"
        
    def __repr__(self):
        return self.__str__()

#INPUT
monkies = []
monkies.append(Monkey(0,[66, 79],'*',11,7,6,7))
monkies.append(Monkey(1,[84, 94, 94, 81, 98, 75],'*',17,13,5,2))
monkies.append(Monkey(2,[85, 79, 59, 64, 79, 95, 67],'+',8,5,4,5))
monkies.append(Monkey(3,[70],'+',3,19,6,0))
monkies.append(Monkey(4,[57, 69, 78, 78],'+',4,2,0,3))
monkies.append(Monkey(5,[65, 92, 60, 74, 72],'+',7,11,3,4))
monkies.append(Monkey(6,[77, 91, 91],'*',None,17,1,7))
monkies.append(Monkey(7,[76, 58, 57, 55, 67, 77, 54, 99],'+',6,3,2,1))
        
# TEST DATA
testMonkies = []
testMonkies.append(Monkey(0,[79, 98],'*',19, 23,2,3))
testMonkies.append(Monkey(1,[54, 65, 75, 74],'+', 6, 19, 2,0))
testMonkies.append(Monkey(2,[79, 60, 97], '*', None, 13, 1,3))
testMonkies.append(Monkey(3,[74], '+', 3, 17, 0,1))

monkies = testMonkies

def monkeyBusiness(levelDivide = 0, rounds=10000):
    for round in range(1,rounds+1):
        for mnkno in range(len(monkies)):
            mnk = monkies[mnkno]
            for i in range(len(mnk.items)):
                mnk.count = mnk.count+1
                itm = mnk.items.pop(0)
                if mnk.val is None:
                    v = itm
                else:
                    v = mnk.val

                if mnk.op == '+':
                    newVal = itm + v
                if mnk.op == '*':
                    newVal = itm * v

                if levelDivide != 0:
                    newVal = newVal // levelDivide

                rest = newVal % mnk.div
                if rest==0:
                    nextMonkey = mnk.ifTrue
                else:
                    nextMonkey = mnk.ifFalse
                monkies[nextMonkey].items.append(newVal)

        if round%100==0:
            print("ROUND", round) 
            #print(monkies)

    cnt = []
    for m in monkies:
        cnt.append(m.count)
    cnt.sort(reverse = True)
    return(cnt[0] * cnt[1])


print("Day10 part1:", monkeyBusiness(3, 20))
#print("Day10 part2:", monkeyBusiness(0, 10000))