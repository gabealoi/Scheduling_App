
class Shift:
    def __init__(self, id, sTime, eTime, duration):
        self.id = id
        self.sTime = sTime
        self.eTime = eTime
        self.duration = duration


    # Getters
    def getID(self):
        return self.id
    
    def getStime(self):
        return self.sTime
    
    def getEtime(self):
        return self.eTime
    
    def getDuration(self):
        return self.duration
    

    # string override
    def __str__(self) -> str:
        formatted_start_time = self.sTime.strftime("%H:%M")
        formatted_end_time = self.eTime.strftime("%H:%M")
        return f"{self.id}\t{formatted_start_time}-{formatted_end_time}\t{self.duration}\n"

        