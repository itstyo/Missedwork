#Tyler Odden
#Project 4
import json
#self to ask the type of control/admin student , max size if needed, and list holder
class Types:
    def __init__(self, type, max_size):
        self.name = type
        self.max_size = max_size
        self.roster = []

    def add_student(self, student_name):
        # Adding student prompts. Making sure the max size can carry the amount of students.
        if len(self.roster) < self.max_size:
            return True
        else:
            return False
# rmoving student in main roster if name is present in list
    def remove_student(self, student_name):
        if student_name in self.roster:
            return True
        else:
            return False
class RegistrationSystem:
    def __init__(self):
        self.classes = {}

    def create_class(self, class_name, max_size):    #Adding class and name and if the name wasn't in the list of classes created then exit
        if class_name not in self.classes:
            self.classes[class_name] = Types(class_name, max_size)
            return True
        else:
            return False

    def update_class(self, class_name, new_max_size):
        if class_name in self.classes:
            self.classes[class_name].max_size = new_max_size #If class name is within self class list then update the new class size
            return True
        else:
            return False

    def print_all_rosters(self):   #Printing off names in list
        for class_name, class_obj in self.classes.items():
            class_obj.print_roster()

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.classes = json.load(file)
            #making sure the file can load and can be worked on after

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.classes, file)
            #Stored information in registrationSystems is in json file

    def enroll_student(self, student_name, class_name):
        # enrolling a student and making sure the class one wants to enroll in is existing
        if class_name in self.classes:
            return self.classes[class_name].add_student(student_name)
        else:
            return False

    def unenroll_student(self, student_name, class_name):
        if class_name in self.classes:
            return self.classes[class_name].remove_student(student_name)
        else:
            return False
        #un enrolling a student and making sure they can be unenrolled and that the class exists

    def print_student_schedule(self, student_name):
        schedule = [class_name for class_name, class_obj in self.classes.items() if
                    student_name in class_obj.roster]
        print(f"{student_name}'s schedule: {schedule}")
        #printing schedule of student name in the registrar system to check if they are in class roster
def main():
    registration_system, data_file = RegistrationSystem(), "registration_data.json"
    try:
        registration_system.load_data(data_file)
    except FileNotFoundError:
        pass

    while True:
        mode = input("Enter mode (admin/student): ")

        if mode == "admin":
            # Administrator mode
            option = input("Enter option (Create/Delete/Update/Print Roster/Save/Quit): ")

            if option == "Create":
                class_name = input("Enter class name: ")
                max_size = int(input("Enter maximum class size: "))
                if registration_system.create_class(class_name, max_size):
                    print("Class created successfully.")
                else:
                    print("Class already exists.")

            elif option == "Delete":
                class_name = input("Enter class name to delete: ")
                if registration_system.delete_class(class_name):
                    print("Class deleted successfully.")
                else:
                    print("Class not found.")

            elif option == "Update":
                class_name = input("Enter class name to update: ")
                new_max_size = int(input("Enter new maximum class size: "))
                if registration_system.update_class(class_name, new_max_size):
                    print("Class updated successfully.")
                else:
                    print("Class not found.")

            elif option == "Print Roster":
                registration_system.print_all_rosters()

            elif option == "Save":
                registration_system.save_data(data_file)
                print("Data saved successfully.")

            elif option == "Quit":
                registration_system.save_data(data_file)
                print("Exiting program.")
                break

            else:
                print("Invalid option.")

        elif mode == "student":
            # Student mode
            option = input("Enter option (enroll/unenroll/Schedule/quit): ")

            if option == "enroll":
                student_name = input("Enter student name: ")
                class_name = input("Enter class name to enroll: ")
                if registration_system.enroll_student(student_name, class_name):
                    print("Enrolled successfully.")
                else:
                    print("Class full or not found.")

            elif option == "unenroll":
                student_name = input("Enter student name: ")
                class_name = input("Enter class name to unenroll: ")
                if registration_system.unenroll_student(student_name, class_name):
                    print("Unenrolled successfully.")
                else:
                    print("Student not found in class.")

            elif option == "Schedule":
                student_name = input("Enter student name: ")
                registration_system.print_student_schedule(student_name)

            elif option == "quit":
                print("Exiting program.")
                break

            else:
                print("Invalid option.")

        else:
            print("Invalid mode.")

main()







