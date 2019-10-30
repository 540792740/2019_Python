class RandomizedSet:
    # 98%
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.init_list = []
        self.hashTable = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashTable:
            self.init_list.append(val)
            self.hashTable[val] = len(self.init_list) - 1
            print(self.init_list)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashTable:
            Index = self.hashTable[val]
            ls = len(self.init_list) - 1
            self.hashTable[self.init_list[-1]] = self.hashTable[val]
            self.init_list[Index], self.init_list[ls] = self.init_list[ls], self.init_list[Index]
            self.init_list.pop()
            self.hashTable.pop(val)
            print(self.init_list, self.hashTable)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.init_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()