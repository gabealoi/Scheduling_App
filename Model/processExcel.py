from .Employee import Employee
import pandas as pd

def readExcel():
    # Path to the Excel file
    # !! RIGHT NOW THIS IS A LOCAL PATH, AFTER IMPLEMENTING THE VIEW, THE FILE SHOULD BE UPLOADED
    # THERE WHERE THE PATH WILL BE GRABBED AS WELL TO BE SENT TO THE CONTROLLER TO HANDLE
    excel_file = r'C:\Users\gaben\OneDrive\Documents\PythonCoding\Scheduling_App\Controller\employee_info.xlsx'
    # excel_file = r'employee_info.xlsx'
    allEmployees = []

    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(excel_file)

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
    except Exception as e:
        print(f"An error has occured in reading your Excel file: {str(e)}")


