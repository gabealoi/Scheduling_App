'''
    This file is the top level script for the controller of the scheduling application.
'''

# The stuff here is to get the interpreter to realize that this directory is a Module, thus giving the ability to import other
# scripts from other directories
import sys
import os

# Get the absolute path of the root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the root directory to the Python module search path
sys.path.append(root_dir)
# end sys path additions


# BEGIN IMPORTS FROM MODEL
from Model.processExcel import generateEmployeeInfoDict, readEmployeesFromExcel, readAvailabilitiesFromExcel
from Model.scheduler import makeSchedule
from Model.writeExcel import writeOutput
import threading, time
# 

def main():
    # ------------------------------------------------------------------------------------------------------------------------------------
    '''
        First thing is first, load in the excel file, provided that it is formatted correctly, into Emp objects
        and make a faux relational database out of the read information
    '''
    # create a thread for the function
    thread = threading.Thread(target=readEmployeesFromExcel)
    thread2 = threading.Thread(target=readAvailabilitiesFromExcel)

    # start the thread
    thread.start()
    thread2.start()
    # while we are waiting for the function to finish, print loading message
    print("Loading Excel file...")

    # once thread completes
    thread.join()
    thread2.join()
    
    # read employees into Employee objects and store them all in a list
    allEmployees = readEmployeesFromExcel()
    allAvailabilities = readAvailabilitiesFromExcel()

    # connect employees with a list of their availabilities
    empInfo = generateEmployeeInfoDict(allEmployees, allAvailabilities)
    print("Finished loading Excel file.")
    # ------------------------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------------------------
    '''
        Next, we'll use this information to run the shceduler model on to generate a schedule
    '''
    schedule = makeSchedule(empInfo)
    # ------------------------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------------------------
    '''
        Lastly, we'll move the list of shifts for the current schedule to be accessed and written to an Excel as output
    '''

    print("..Generating Schedule")
    writeOutput(schedule, allEmployees)
    print("Schedule Generated")
    # ------------------------------------------------------------------------------------------------------------------------------------

    



if __name__ == "__main__":
    main()