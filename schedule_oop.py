import pickle
from prettytable import PrettyTable

class SchedulePlanner:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity, time):
        self.activities.append((activity, time))

    def view_schedule(self):
        if not self.activities:
            print("No activities in the schedule.")
            return

        table = PrettyTable()
        table.field_names = ["Activity", "Time"]

        for activity, time in self.activities:
            table.add_row([activity, time])

        print(table)

    def delete_activity(self, activity):
        found = False
        for item in self.activities:
            if item[0] == activity:
                self.activities.remove(item)
                print(f"Activity '{activity}' deleted from the schedule.")
                found = True
                break

        if not found:
            print(f"Activity '{activity}' not found in the schedule.")

        self.save_to_file()  # Save updated data to the file

    def delete_all_activities(self):
        self.activities = [] #creates empty list which deletes existing data
        self.save_to_file() #deletes existing data in the file

    def save_to_file(self):
        with open('schedule_planner.pkl', 'wb') as file:
            pickle.dump(self.activities, file)

    def load_from_file(self):
        try:
            with open('schedule_planner.pkl', 'rb') as file:
                self.activities = pickle.load(file)
                print("Schedule data loaded from file.")
        except FileNotFoundError:
            print("No saved schedule data found.")

def main():
    schedule_planner = SchedulePlanner()

    # Load existing schedule data from the file (if available)
    schedule_planner.load_from_file()

    while True:
        print("--- Schedule Planner ---")
        print("[A] Add Activity")
        print("[B] View Schedule")
        print("[C] Delete Activity")
        print("[Q] Quit")

        choice = input("Enter your choice: ")

        if choice.lower() == 'a':
            activity = input("Enter the Activity Name: ")
            time = input("Enter the Time of Activity: ")
            schedule_planner.add_activity(activity, time)
            print("Activity added to the schedule.")
            schedule_planner.save_to_file()  # Save updated data to the file

        elif choice.lower() == 'b':
            schedule_planner.view_schedule()

        elif choice.lower() == 'c':
            ques = input("[1] Delete All Activities\
                     \n[2] Delete Specific Activity\
                     \nYour Choice? : ")
            
            if  ques == '2':
                activity_to_delete = input("Enter the Activity Name to delete: ")
                schedule_planner.delete_activity(activity_to_delete)

            elif ques == '1':
                if input("Are you sure you want delete all activities? [y/n] :") != 'n':
                    schedule_planner.delete_all_activities()
                    print("All activties deleted!")
                else:
                    break

            else:
                return "Invalid Choice!" 

        elif choice.lower() == 'q':
            print("See you Later!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
        
        if input("Do you want to continue? [y/n] : ") != 'y':
            schedule_planner.save_to_file()
            break
        

if __name__ == "__main__":
    main()
