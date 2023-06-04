
class Availability:
    def __init__(self, id, dow, sTime, eTime):
        self.id = id
        self.dow = dow
        self.sTime = sTime
        self.eTime = eTime


    # getters
    def getID(self):
        return self.id
    
    def getDOW(self):
        return self.dow
    
    def getsTime(self):
        return self.sTime
    
    def geteTime(self):
        return self.eTime
    

    # toStr override
    def __str__(self) -> str:
        return f"{self.id} :: {self.dow} :: {self.sTime}-{self.eTime}"