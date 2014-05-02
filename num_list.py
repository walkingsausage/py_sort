import sys
import random


class num_list:
    my_list = []

    def __init__(self, size):
        random.seed()
        i = 0
        while i < size:
            self.my_list.append(random.randint(0, sys.maxint))
            i += 1

    def getList(self):
        return self.my_list