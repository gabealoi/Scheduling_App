from .Employee import Employee
from .Shifts import Shift
from datetime import datetime, timedelta
import random

 
# Initialize dictionary to store scheduled shifts
schedule = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}


def makeSchedule(empInfo=dict):
    # Create a dictionary to store scheduled shifts for each employee
    employeeShifts = {employee: [] for employee in empInfo.keys()}

    # Create a list of available employees for each day
    availableEmployees = {day: [] for day in schedule.keys()}
    for emp, avas in empInfo.items():
        for ava in avas:
            if ava.getDOW() != None:
                availableEmployees[ava.getDOW()].append(emp)


    # Create lists of opening and closing shift times
    opening_shift_times = ["08:15", "09:00", "09:30", "10:00", "10:30", "11:00"]
    closing_shift_times = ["15:00", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00"]
    shift_duration = [4, 4.5, 5, 6, 6.5, 7, 7.5, 8]


    # Iterate over each day of the week
    for day, employees in availableEmployees.items():
        # Shuffle the list of available employees for randomness
        random.shuffle(employees)

        # Initialize lists for opening and closing shifts
        openers = []
        closers = []
                
        # Iterate until we have 2 openers and 2 closers
        while len(openers) < 2 or len(closers) < 2:
            # Check if there are no more employees available for the day
            if not employees:
                break
            
            # Select an employee from the available employees list
            employee = employees.pop(0)
            
            # Get the employee's age and requested shift duration
            age = employee.getAge()

            duration = 0
            if age < 18:
                duration = random.choice(shift_duration[:4])  # Convert duration to integer
            else:
                duration = random.choice(shift_duration[3:])
            
            # Determine if the employee can work an opening or closing shift
            if len(openers) < 2:
                shift_times = opening_shift_times
                shift_type = "opener"
            else:
                shift_times = closing_shift_times
                shift_type = "closer"
            
            # Iterate over the shift times and try to assign a shift
            for shift_time in shift_times:
                start_time = datetime.strptime(shift_time, "%H:%M")

                # set to desired day of the week
                current_day = start_time.strftime("%A")
                while current_day != day:
                    start_time += timedelta(days=1)
                    current_day = start_time.strftime("%A")

                end_time = start_time + timedelta(hours=duration)

                
                # Check if the shift end time goes beyond 12am
                if end_time.replace(hour=0, minute=0, second=0, microsecond=0) <= end_time < end_time.replace(hour=8, minute=15, second=0, microsecond=0):
                    end_time = datetime.strptime("00:00", "%H:%M")
                    dMins = abs(end_time.minute - start_time.minute) / 60
                    duration = 12 - (abs(end_time.hour - start_time.hour) - 11 + dMins)

                # Create a shift object
                shift = Shift(employee.getID(), start_time, end_time, duration)
                
                # Check if the employee is available during the shift time
                if isEmployeeAvailable(employee, shift, empInfo):
                    # Assign the shift to the employee and add to the schedule
                    employeeShifts[employee].append(shift)
                    schedule[day].append(shift)
                    
                    # Add the employee to the appropriate list
                    if shift_type == "opener":
                        openers.append(employee)
                    else:
                        closers.append(employee)
                    
                    break
        

    return schedule




def isEmployeeAvailable(employee, shift, empInfo):
    empAvailabilities = empInfo[employee]  # Get the employee's availabilities
    shiftStartTime = shift.getStime()  # Get the start time of the shift
    shiftEndTime = shift.getEtime()  # Get the end time of the shift
    
    
    for availability in empAvailabilities:
        if availability.getDOW() == shiftStartTime.strftime("%A"):
            # Check to see if the employee is even available on that day
            if availability.getsTime() == None:
                return False
            else:
                # Check if the shift falls within the employee's availability
                if availability.getsTime() <= shiftStartTime.time() and availability.geteTime() >= shiftEndTime.time():
                    # Check if the employee is already scheduled for another shift on the same day
                    for scheduledShiftList in schedule.values():
                        for scheduledShift in scheduledShiftList:
                            if scheduledShift.getStime().date() == shiftStartTime.date() and scheduledShift.getEtime().date() == shiftEndTime.date() and employee.getID() == scheduledShift.getID():
                                return False
                            
                    # ensure employee is not exceeded total requested hours
                    if (getEmpTotalHours(employee) + shift.getDuration()) > employee.getHours():
                        return False
                
                    return True
                
    
    return False

                    
                    
def getEmpTotalHours(employee=Employee):
    totalHours = 0

    for shifts in schedule.values():
        for shift in shifts:
            if shift.getID() == employee.getID():
                totalHours += shift.getDuration()

    return totalHours


