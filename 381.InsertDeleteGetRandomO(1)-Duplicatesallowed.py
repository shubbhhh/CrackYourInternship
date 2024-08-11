class RandomizedCollection:

    def __init__(self):
        self.collection = []
        self.collMap = defaultdict(set)

    def insert(self, val: int) -> bool:
        if val in self.collMap and len(self.collMap[val]) > 0:
            res = False
        else:
            res = True

        self.collection.append(val)
        self.collMap[val].add(len(self.collection)-1)

        return res

    def remove(self, val: int) -> bool:
        if val in self.collMap and len(self.collMap[val]) > 0:
            rmInd = self.collMap[val].pop()
            lstIndColl = len(self.collection) - 1
            lstVal = self.collection[lstIndColl]
            self.collMap[lstVal].add(rmInd)
            self.collMap[lstVal].remove(lstIndColl)

            self.collection[rmInd], self.collection[lstIndColl] = self.collection[lstIndColl], self.collection[rmInd]

            self.collection.pop()
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.collection)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()