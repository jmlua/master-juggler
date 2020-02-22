'''
Given a list of numbers in any order, return a sorted list (in ascending order). Restrictions:
a. You can only go through the list of numbers once. 
b. At most two stacks can be used to store the number temporarily.
c. The output list should be used to store the result only. 
d. Sorting has to be stable.
'''


from abc import ABC, abstractmethod     #Abstract Base Class
from StackBase import StackBase
from StackList import StackList


def makeSorted(input):
    """
    [input] is a list of numbers

    This function print the list of numbers in ascending order.

    Restriction: Touch each number ONCE and no additional data structures 
    """
    sortedS = StackList() 
    tmpS = StackList()
    result = []

    for num in input:
        if sortedS.isEmpty() == True:
            sortedS.push(num)
        else:
            if num < sortedS.getTop():
                sortedS.push(num)
            elif num >= sortedS.getTop():
                while num >= sortedS.getTop():
                    tmp.push(sortedS.getTop())
                    sortedS.pop()
                sortedS.push(num)
                while num >= tmp.getTop():
                    sortedS.push(tmp.getTop())
                    tmp.pop()               
    while sortedS.size() > 0:
        result.append(sortedS.getTop())
        sortedS.pop()
    return result


def main():
    sList = input("Give a list of numbers: ").split(" ")
    numList = input


if __name__ == "__main__":
    main()
