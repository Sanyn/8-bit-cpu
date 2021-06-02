class RAM:
    mem=[]
    size=0
    def __init__(self,s,ini):
        self.size=int(s)
        if(ini == "noin"):
            for i in range(int(s)):
                self.mem.append(0)
        else:
            rf = open(ini, "r")
            for i in range(int(s)):
                self.mem.append(int(rf.readline()))
    def clr(self):
        for i in range(self.size):
            self.mem[i]=0
    def get(self,addr):
        return self.mem[int(addr)]
    def set(self,addr, val):
        self.mem[int(addr)]=int(val)