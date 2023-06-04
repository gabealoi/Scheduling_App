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

from Model import scheduler, processExcel
import threading

def main():
    # ------------------------------------------------------------------------------------------------------------------------------------
    '''
        First thing is first, load in the excel file, provided that it is formatted correctly, into Emp objects
        and make a faux relational database out of the read information
    '''
    # create a thread for the function
    thread = threading.Thread(target=processExcel.readExcel)

    # start the thread
    thread.start()
    # while we are waiting for the function to finish, print loading message
    print("Loading Excel file...")

    # once thread completes
    thread.join()
    
    # read employees into Employee objects and store them all in a list
    allEmployees = processExcel.readExcel()
    print("Finished loading Excel file.")
    # ------------------------------------------------------------------------------------------------------------------------------------







    # ------------------------------------------------------------------------------------------------------------------------------------
    '''
        Next, we'll use this information to run the shceduler model on to generate a schedule
    '''
    # ------------------------------------------------------------------------------------------------------------------------------------
    




























    '''
        Lastly, we'll move the list of shifts for the current schedule to be accessed and written to an Excel as output
    '''
    
    





if __name__ == "__main__":
    main()