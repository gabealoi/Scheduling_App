import dbConnect
from Employee import Employee
from Availability import Availability

def processEmps():
    allEmployees = []
    dbEmps = dbConnect.getEmps()

    for info in dbEmps:
        if info != None:
            newEmp = Employee(info[0], info[1], info[2], info[3])
            allEmployees.append(newEmp)

    return allEmployees

def processAvas():
    allAvailabilities = []
    dbAvas = dbConnect.getAvailabilities()

    day = 0
    weekAva = []
    for info in dbAvas:
        if info != None:
            newAva = Availability(info[0], info[1], info[2], info[3])
            weekAva.append(newAva)

        day+=1

        # reset every 7 days, append list of list
        if day == 7:
            allAvailabilities.append(weekAva)
            day = 0
            weekAva = []
    

    return allAvailabilities
    
