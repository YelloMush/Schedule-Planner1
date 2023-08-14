import pandas as pd 
import pickle

try:
    with open('schedule_planner.pkl','rb') as file:
        saved_data = pickle.load(file)
        ACTIVITY = saved_data['activity']
        TIME = saved_data['time']
except FileNotFoundError:
    ACTIVITY = []
    TIME = []



class ClassSchedule:
    def __init__(self, activity, timing):
        self.activity = activity
        self.timing = timing 
    
    def display_schdle(self):
        print(f'Acitvity: {self.activity}, Time: {self.timing}')

while True:
    ques = input("---Select one:--- \n(A) Create a new schedule \
                 \n(B) View Existing Schedule \
                 \n(C) Delete Existing Data \n(Q) Quit \nYour Choice?: ")
    
    if ques.lower() == 'q':

        data_to_save = {
            'activity': ACTIVITY,
            'time': TIME
        }
        with open('schedule_planner.pkl', 'wb') as file:
            pickle.dump(data_to_save, file)

        break

    elif ques.lower() == 'a':
        act = input("Enter an Activity: ")
        time = input("Enter time of activity: ")
        sch = ClassSchedule(act, time)
        ACTIVITY.append(act)
        TIME.append(time)

    elif ques.lower() == 'b':
        df = pd.DataFrame({
            "Activity": ACTIVITY,
            "Time": TIME
        })
        print(df)

    elif ques.lower() == 'c':

        df = pd.DataFrame({
            "Activity": ACTIVITY,
            "Time": TIME
        })
        print(df)

        delete_data = int(input("Enter the row index to delete the row: "))

        deleted_df = df.drop(delete_data)
        print(deleted_df)

    else:
        print("Invalid Choice. Please select 'A', 'B' or 'Q'")
    
    if input('Do You Want To Continue? [y/n]') != 'y':

        data_to_save = {
            'activity': ACTIVITY,
            'time': TIME
        }
        with open('schedule_planner.pkl', 'wb') as file:
            pickle.dump(data_to_save, file)

        break   
