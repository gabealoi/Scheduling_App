'''
    This file is the top level script for the models. It is used for development in order to test the Model's logic with faux data.
'''
import processDB
import scheduler

def main():
    # gather all emp obj's
    allEmps = processDB.processEmps()
    allAvas = processDB.processAvas()
    
    # generate a dictionary attaching an Emp obj key to a availability list
    empTime = {}
    for i in range(0, len(allEmps)):
        empTime[allEmps[i]] = allAvas[i];


    schedule = scheduler.makeSchedule(empTime)

    for dow, sch in schedule.items():
        print(dow)
        print(("").join(str(days) for days in sch))


if __name__ == "__main__":
    main()