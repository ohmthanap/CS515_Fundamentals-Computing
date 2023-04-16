# Thanapoom Phatthanaphan
# This is the Counter class.

class Counter(object):

    def __init__(self):
        """Sets up the counter"""
        self.reset()

    def reset(self):
        """Returns the counter to 0"""
        self.value = 0

    def getValue(self):
        """Returns the value of the counter"""
        return self.value

    def increment(self, amount = 1):
        """Adds amount to the counter"""
        self.value += amount
        return self.value

    def decrement(self, amount = 1):
        """Subtracts amount from the counter"""
        self.value -= amount
        return self.value

    def __str__(self):
        """Returns the value of the counter as string"""
        return str(self.value)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.value == other.value
