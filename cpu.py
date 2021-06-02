from graphics import *
from gpu import *
from ram import *
from rom import *
from register import *
from datetime import datetime
import math

class CPU:
    def __init__(self,freq):
        self.regA = register(0)
        self.regB = register(0)
        self.memAdrReg = register(0)
        self.argReg = register(0)
        self.instReg = register(0)
        self.progCounter = counter(0,256)
        self.stepper = counter(0,16)
        self.BUS = register(0)
        self.outputReg = register(0)
        
        self.hlt = False
        self.nullflag = False
        
        self.ram = RAM(256,"ram.txt")
        self.rom = ROM(8192)
        
        self.frequency = freq
        self.deltaTime = round(1000/freq)
        
    def updateFlag(self):
        if(self.regA.get() == 0):
            self.nullflag = True
        else:
            self.nullflag = False
    
    def execute(self):
        while(not self.hlt):
            dt = datetime.now().microsecond
            command = self.rom.get(self.nullflag*4096+self.instReg.get()*16+self.stepper.get())
            if(command == 0):
                pass
            elif(command == 1):
                self.regA.set(self.BUS.get())
            elif(command == 2):
                self.BUS.set(self.regA.get())
            elif(command == 3):
                self.regB.set(self.BUS.get())
            elif(command == 4):
                self.BUS.set(self.regB.get())
            elif(command == 5):
                self.regA.set(self.regA.get()+self.regB.get())
            elif(command == 6):
                self.regA.set(self.regA.get()-self.regB.get())
            elif(command == 7):
                self.memAdrReg.set(self.BUS.get())
            elif(command == 8):
                self.argReg.set(self.BUS.get())
            elif(command == 9):
                self.BUS.set(self.argReg.get())
            elif(command == 10):
                self.progCounter.set(self.BUS.get())
            elif(command == 11):
                self.BUS.set(self.progCounter.get())
            elif(command == 12):
                self.progCounter.inc()
            elif(command == 13):
                self.outputReg.set(self.BUS.get())
            elif(command == 14):
                self.BUS.set(self.ram.get(self.memAdrReg.get()))
            elif(command == 15):
                self.ram.set(self.memAdrReg.get(),self.BUS.get())
            elif(command == 16):
                self.instReg.set(self.BUS.get())
            elif(command == 17):
                self.hlt=True;
            self.updateFlag()
            self.stepper.inc()
            print(self.outputReg.get())
            dt = datetime.now().microsecond-dt
            if(dt<0):
                dt+=1000
            if(dt < self.deltaTime):
                time.sleep((self.deltaTime-dt)/1000)