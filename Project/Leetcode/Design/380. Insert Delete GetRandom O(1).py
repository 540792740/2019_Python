class RandomizedSet:
    # 98%

    def __init__(self):
        self.dic = {}
        self.init_list = []

    def insert(self, val):
        if val not in self.dic:
            self.dic[val] = len(self.init_list)
            self.init_list.append(val)
            return True
        else:
            return False

    def remove(self, val):
        if val in self.dic:
            index = self.dic[val]
            ls = len(self.init_list) - 1
            self.dic[self.init_list[-1]] = self.dic[val]
            self.init_list[index] = self.init_list[-1]
            self.init_list.pop()
            self.dic.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        return random.choice(self.init_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

dic = set()
dic.add(1)
dic.add(2)
dic.add(3)
dic = list(dic)
print(dic)