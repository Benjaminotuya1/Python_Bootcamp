from herbal import herbal_remedies
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f'{self.name} is {self.age} old')

class Patient(Person):
    def __init__(self, name,age,illness):
        super().__init__(name,age)
        self.illness = illness
        self.bill = 0
        self.id = 'P1'

class Doctor(Person):
    def __init__ (self, name,age,specialization):
        super().__init__(name,age)
        self.specialization = specialization
        self.patients = []

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
    
    def admit_patient(self, patient):
        self.patients.append(patient)
        print(f'Admitted patient: {patient.name}')

    def hire_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f'Hired staff: Dr {doctor.name} {(doctor.specialization)}')

    def consult_ai(self, patient):
        print(f'\n--- AI CONSULTATION FOR {patient.name} ---')
        if patient.illness in herbal_remedies:
            cure = herbal_remedies[patient.illness]
            print(f'AI Diagnosis: Mild case of {patient.illness}.')
            print(f'Recomendation: {cure}')
        else:
            print(f'AI Diagnosis: {patient.illness} is unknown or severe.')

            if self.doctors:
                assigned_doc = self.doctors[0]
                print(f'Referral: pls see Dr. {assigned_doc.name} {assigned_doc.specialization}.')
            else:
                print("Referral: Please go to the nearest General Hospital (No doctors available here).") 



# my_hospital = Hospital('St. Benjamin Teaching Hospital')
# p1 = Patient('Ali', 29, 'Flu')
# dr_ben = Doctor('Benjamin', 45, 'Neurosurgon',)
# my_hospital.admit_patient(p1)
# my_hospital.hire_doctor(dr_ben)


# p2 = Patient('Zara', 35, 'Nausea')
# my_hospital.consult_ai(p2)
# my_hospital.consult_ai(p1)
