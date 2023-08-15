import pandas as pd 
import pickle
from prettytable import PrettyTable


class SchedulePlanner:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity, time):
        self.activities.append((activity, time))

    def view_schedule(self):
        if not self.activities:
            print("No activities in the schedule")
            return
        
        table = PrettyTable()
        table.field_names = ['Acitvity', 'Time']

        for activity, time in self.activities:
            table.add_row([activity, time])

        print(table)

    def delete_activity(self, activity):
        for item in self.activities:
            if item[0] == activity:
                self.activities.remove(item)
            print(f"Activity {activity} succesfully deleted!")
        print(f"Activity {activity} not found!")
        return
    
    def save_to_file(self):
        with open('schedule_planner.pkl', 'wb') as file:
            pickle.dump(self.activities, file)

    def load_to_file(self):
        try:
            with open('schedule_planner.pkl', 'rb') as file:
                pickle.load(file)
                print("Schedule Data loaded from file")
        except FileNotFoundError:
            print("No saved schedule data exist!")
def main():
    schedule_planner = SchedulePlanner()
    schedule_planner.load_to_file()

    
#class ClassSchedule:
#    def __init__(self, activity, timing):
#        self.activity = activity
#        self.timing = timing 
#    
#    def display_schdle(self):
#        print(f'Acitvity: {self.activity}, Time: {self.timing}')

while True:
    ques = input("--- Select one: --- \
                 \n(A) Create a new activity \
                 \n(B) View Existing Schedule \
                 \n(C) Delete Existing Data \
                 \n(Q) Quit \
                 \nYour Choice?: ")
    
#    if ques.lower() == 'q':
#
#        data_to_save = {
#            'activity': ACTIVITY,
#            'time': TIME
#        }
#        with open('schedule_planner.pkl', 'wb') as file:
#            pickle.dump(data_to_save, file)
#
#        break

    if ques.lower() == 'a':
        activity = input("Enter the Activity Name: ")
        time = input("Enter the Time of Activity: ")

        SchedulePlanner.add_activity(activity, time)
        print("Activity added to the schedule")
        SchedulePlanner.save_to_file()

    elif ques.lower() == 'b':
        SchedulePlanner.view_schedule()

    elif ques.lower() == 'c':

        acitvity_to_delete = input("Enter Activity Name to delete: ")
        SchedulePlanner.delete_activity(acitvity_to_delete)

    elif ques.lower() == 'q':
        print('See you Later!')
        break

    else:
        print("Invalid Choice. Please select 'A', 'B' or 'Q'")
    
    if input('Do You Want To Continue? [y/n]') != 'y':
        SchedulePlanner.save_to_file()  

if __name__ == "__main__":
    main()