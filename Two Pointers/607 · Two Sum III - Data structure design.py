import collections
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.table = collections.defaultdict(int)

    def add(self, number):
        self.table[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        for number in self.table:
            if value - number in self.table:
                if (value - number != number) or (value - number == number and self.table[number] > 1):
                    return True
        return False

