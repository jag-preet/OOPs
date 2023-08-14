#Performed by: Jagpreet Singh 
#Date:10 August 2023
#This is the Final Group Project which will explain us
#about some patients who have some problems so they concerns different types of Doctors
#Submitted to : Kenneth Lai Sir

#This will help us to understand how I created Different types of Data
#Firstly data of Doctor is Displayed in the code
       

class Doctor():
    def __init__(self, id, name, speciality, timing, qualification, room_no):
        self.id = id
        self.name = name 
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.room_no = room_no


#Now This Part will Explain how we created names , disease , gender , age of Patients

class Patient():
    def __init__(self, id, name, disease, gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age


# THis below coding Part will Explain us about the Doctors details

def display_doctors(doctors):
    
    for doctor in doctors:
        print(f"{doctor.id:<5} {doctor.name:<22} {doctor.speciality:<15} {doctor.timing:<15} {doctor.qualification:<15} {doctor.room_no}")

# This section will Tell us about Patients information needed for doctors to identify various patients.


def display_patients(patients):
   
    for patient in patients:
        print(f"{patient.id:<5} {patient.name:<22} {patient.disease:<15} {patient.gender:<15} {patient.age}")


#Here we will Search Doctor By ID:


def search_doctor_by_id(doctors, doctor_id):
    for doctor in doctors:
        if doctor.id == doctor_id:
            return doctor
    return None


#Here we will search doctor By name
def search_doctor_by_name(doctors, name):
    for doctor in doctors:
        if doctor.name.lower() == name.lower():
            return doctor
    return None


#This Part will Search Patients by their well proved ID:



def search_patient_by_id(patients, patient_id):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    return None


#This Below Part will Tell us about all important Procedures like how both files of Doctor and Patients get extracted and
#  how Main Menu and Sub menu will appear by following different methods

def main():
    doctors = []
    patients = []

    with open('Doctors.txt', 'r') as doctors_file:
        for line in doctors_file:
            data = line.strip().split('_')
            doctors.append(Doctor( data[0], data[1], data[2], data[3], data[4], data[5]))

    with open('Patients.txt', 'r') as patients_file:
        for line in patients_file:
            data = line.strip().split('_')
            patients.append(Patient(data[0], data[1], data[2], data[3], data[4]))

    while True:
        print("\nWelcome to Alberta Hospital (AH) Management system")
        print("Select from the following options, or select 3 to stop:")
        print("1 - Doctors\n2 - Patients\n3 - Exit Program")

        MainMenu = int(input(" >>> "))

        if MainMenu == 1:
            while True:
                print("\nDoctors Menu:")
                print("1 - Display Doctors list\n2 - Search for doctor by ID")
                print("3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu")
                
                Sub_menu= int(input(" >>> "))
                
                if Sub_menu == 1:
                    display_doctors(doctors)
                elif Sub_menu == 2:
                    id = input("Enter the doctor Id: ")
                    doctor = search_doctor_by_id(doctors, id)
                    if doctor:
                        display_doctors([doctor])
                    else:
                        print("Can't find the doctor with the same ID on the system")
                elif Sub_menu == 3:
                    doctor_name = input("Enter the doctor name: ")
                    doctor = search_doctor_by_name(doctors, doctor_name)
                    if doctor:
                        display_doctors([doctor])
                    else:
                        print("Can't find the doctor with the same name on the system")
                elif Sub_menu == 4:
                    id = input("Enter the doctor’s ID: ")
                    doctor_name = input("Enter the doctor’s name: ")
                    speciality = input("Enter the doctor’s specility: ")
                    timing = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
                    qualification = input("Enter the doctor’s qualification: ")
                    room_no = input("Enter the doctor’s room no: ")
                    doctors.append(Doctor(id, doctor_name, speciality, timing, qualification, room_no))
                    print(f"Doctor whose ID is {id} has been added")
                elif Sub_menu == 5:
                    id = input("Please enter the id of the doctor that you want to edit their information: ")
                    doctor = search_doctor_by_id(doctors, id)
                    if doctor:
                        print(f"Editing doctor with ID: {id}")
                        new_name = input("Enter new Name: ")
                        another_speciality = input("Enter new Specilist in: ")
                        new_timing = input("Enter new Timing: ")
                        another_qualification = input("Enter new Qualification: ")
                        new_room_number = input("Enter new Room number: ")
                        doctor.name = new_name
                        doctor.speciality = another_speciality
                        doctor.timing = new_timing
                        doctor.qualification = another_qualification
                        doctor.room_number = new_room_number
                        print(f"Doctor whose ID is {id} has been edited")
                    else:
                        print("Can't find the doctor with the same ID on the system")
                elif Sub_menu == 6:
                    break
        
        elif MainMenu == 2:
            while True:
                print("\nPatients Menu:")
                print("1 - Display patients list\n2 - Search for patient by ID")
                print("3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu")
                
                Sub_menu = int(input("  "))
                
                if Sub_menu == 1:
                    display_patients(patients)

                elif Sub_menu == 2:
                    patient_id = input("Enter the Patient Id: ")
                    patient = search_patient_by_id(patients, patient_id)
                    if patient:
                        display_patients([patient])
                    else:
                        print("Can't find the Patient with the same id on the system")
                elif Sub_menu == 3:
                    patient_id = input("Enter Patient id: ")
                    patient_name = input("Enter Patient name: ")
                    disease = input("Enter Patient disease: ")
                    gender = input("Enter Patient gender: ")
                    age = input("Enter Patient age: ")
                    patients.append(Patient(patient_id, patient_name, disease, gender, age))
                    print(f"Patient whose ID is {patient_id} has been added")
                elif Sub_menu == 4:
                    patient_id = input("Please enter the id of the Patient that you want to edit their information: ")
                    patient = search_patient_by_id(patients, patient_id)
                    if patient:
                        print(f"Editing patient with ID: {patient_id}")
                        new_name = input("Enter new Name: ")
                        new_disease = input("Enter new disease: ")
                        new_gender = input("Enter new gender: ")
                        new_age = input("Enter new age: ")
                        patient.name = new_name
                        patient.disease = new_disease
                        patient.gender = new_gender
                        patient.age = new_age
                        print(f"Patient whose ID is {patient_id} has been edited")
                    else:
                        print("Can't find the patient with the same ID on the system")
                elif Sub_menu == 5:
                    break
        
        elif MainMenu == 3:
            print("Thanks for using the program. Bye!")
            break



#NOW AT THE END, This FILE WILL ONLY RUN IF THE FILE NAME IS "main.py"



if __name__ == "__main__":
    main()


