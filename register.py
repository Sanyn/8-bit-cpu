class register:
    def __init__(self,val):
        self.value = val
    def clr(self):
        self.value = 0
    def get(self):
        return self.value
    def set(self, val):
        self.value=int(val)
        
class counter:
    def __init__(self,val,maxv):
        self.value = val
        self.maxvalue = maxv
    def clr(self):
        self.value = 0
    def get(self):
        return self.value
    def set(self, val):
        self.value=int(val)
    def inc(self):
        self.value += 1
        if(self.value == self.maxvalue):
            self.value = 0