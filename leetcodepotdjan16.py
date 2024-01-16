lass RandomizedSet:

    def __init__(self):
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val not in self.l:
            self.l.append(val)
            return True
        return False    

    def remove(self, val: int) -> bool:
        if val in self.l:
            self.l.remove(val)
            return True
        return False    

    def getRandom(self) -> int:
        d = random.randint(0,len(self.l)-1)
        return self.l[d]