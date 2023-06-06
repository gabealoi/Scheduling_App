import pandas as pd
from datetime import datetime
import os, subprocess

def writeOutput(schedule=dict, emps=list):
    # format the schedule dict
    fSchedule = formatSchedule(schedule, emps)

    # create pandas dataframe
    df = pd.DataFrame(fSchedule)
    

    # create a pandas Excel writer
    output_directory = f"C:/Users/{os.getlogin()}/Downloads"
    full_path_with_name = os.path.join(output_directory, f'schedule_{str(datetime.now().date())}.xlsx')
    output_excel = pd.ExcelWriter(full_path_with_name)


    # Iterate over each day and shifts in the schedule data
    for day, shifts in fSchedule.items():
        # Create a DataFrame for the current day
        df = pd.DataFrame(shifts)

        # Set the column order
        columns = ['ID', 'Name', 'Start_Time', 'End_Time', 'Duration']
        df = df.reindex(columns=columns)

        # Write the DataFrame to the Excel file with a sheet name
        df.to_excel(output_excel, sheet_name=day, index=False)


        # Auto-fit the columns to fit the content
        worksheet = output_excel.sheets[day]
        for column in worksheet.columns:
            max_length = 0
            column_name = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except TypeError:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            worksheet.column_dimensions[column_name].width = adjusted_width


    output_excel.close()

    # open download directory after generating Excel file
    subprocess.Popen(['explorer', output_directory.replace('/', '\\')])




def formatSchedule(sch=dict, emps=list):
    # predefined column names
    cols = ['ID', 'Name', 'Start Time', 'End Time', 'Duration']

    formatted_Sch = {}

    for dow, shifts in sch.items():
        formatted_Sch[dow] = []

        for s in shifts:
            emp = next((e for e in emps if e.getID() == s.getID()), None)    
            # grab emp name to fill into shift dict
            shift = s.toDict()
            shift['Name'] = emp.getName()
        
            formatted_Sch[dow].append(shift)
            # for header in range(0, len(cols)):
                # formatted_Sch[dow][cols[header]].append(s.getID() if header==0 else emp.getName() if header==1 else s.getStime() if header==2 else s.getEtime() if header==3 else s.getDuration() if header==4 else -1)
                

    return formatted_Sch

    