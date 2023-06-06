from .Employee import Employee
from .Availability import Availability
import pandas as pd
from datetime import datetime

 # Path to the Excel file
# !! RIGHT NOW THIS IS A LOCAL PATH, AFTER IMPLEMENTING THE VIEW, THE FILE SHOULD BE UPLOADED
# THERE WHERE THE PATH WILL BE GRABBED AS WELL TO BE SENT TO THE CONTROLLER TO HANDLE
excel_file = r'C:\Users\gaben\OneDrive\Documents\PythonCoding\Scheduling_App\Controller\employee_info.xlsx'


'''
    Parameters: None
    Description: Reads in employee information from a particularly formatted Excel file
    Returns: List of Employee class objects
'''
def readEmployeesFromExcel():
    # excel_file = r'employee_info.xlsx'
    allEmployees = []
    sheet_index = 0 #reading from the first sheet, which is supposed to just be the employee information

    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(excel_file, sheet_name=sheet_index)

        # Store each column as a separate list
        id_list = df['ID'].tolist()
        name_list = df['Name'].tolist()
        age_list = df['Age'].tolist()
        hours_list = df['Hours'].tolist()

        # Make employee objects of information
        for i in range(0, len(id_list)):
            emp = Employee(id_list[i], name_list[i], age_list[i], hours_list[i])
            allEmployees.append(emp)

        # for e in allEmployees:
        #     print(e)

        return allEmployees


    except FileNotFoundError:
        print("Error: The specified Excel file was not found.\nPlease ensure the selected file exists and is not currently open.")
    except PermissionError:
        print("Error: Please ensure you have the Excel file closed when running this application.")
    except Exception as e:
        print(f"An error has occured in reading your Excel file: {str(e)}")



'''
    Parameters: None
    Description: Reads in availabilities from an Excel file's SECOND sheet
    Return: returns a list of Availability objects
'''
def readAvailabilitiesFromExcel():
    sheet_index = 1 # reading from the SECOND sheet now, which is a specifically formatted Excel file

    try:
        # read excel file into dataframe
        df = pd.read_excel(excel_file, sheet_name=sheet_index)

        # initialize empty list to store every row
        allAvals = []

        # iterate over the rows (excluding the first one)
        for index, row in df.iterrows():
            # get the values of the row, excluding the first col
            avalInfo = row.tolist()


            # make an availability object of the information
            aval = Availability(avalInfo[0], avalInfo[1], None if type(avalInfo[2]) == float else avalInfo[2], None if type(avalInfo[3]) == float else avalInfo[3])
            allAvals.append(aval)

        return allAvals



    except FileNotFoundError:
        print("Error: The specified Excel file was not found.\nPlease ensure the selected file exists and is not currently open.")
    except PermissionError:
        print("Error: Please ensure you have the Excel file closed when running this application.")
    except Exception as e:
        print(f"An error has occured in reading your Excel file: {str(e)}")



'''
    Parameters: empList, avalList
    Description: Helper function to be called by controller to aggregate the data that was parsed from the Excel using the above functions
    Return: Dictionary relating every employee to their weekly availability list
'''
def generateEmployeeInfoDict(allEmployees=list, allAvailabilities=list):
    allEmpInfo = {}
    for emp in allEmployees:
        # initialize empty aval-list for every employee
        allEmpInfo[emp] = []
        for aval in allAvailabilities:
            if emp.getID() == aval.getID():
                allEmpInfo[emp].append(aval)

    return allEmpInfo