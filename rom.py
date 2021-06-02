class ROM:
    mem=[]
    size=0
    def __init__(self,s):
        self.size=int(s)
        rf = open("rom.txt", "r")
        for i in range(int(s)):
            self.mem.append(int(rf.readline()))
    def clr(self):
        for i in range(self.size):
            self.mem[i]=0
    def get(self,addr):
        return self.mem[int(addr)]