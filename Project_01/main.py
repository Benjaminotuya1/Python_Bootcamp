# A class is a blueprint for creating objects.
class Patient:
    # The __init__ method is the constructor. It runs automatically
    # whenever you create a new object from this class.
    # 'self' refers to the object being created.
    def __init__(self, patient_id, name, age, condition, status):
        self.id = patient_id
        self.name = name
        self.age = age
        self.condition = condition
        self.status = status
    def update_status(self, new_status):
        self.status = new_status
        print(f"Patient {self.name} is now {new_status}")

    @classmethod
    def patient_details(cls):
        p_id = input('ID: ')
        p_name = input('Name: ')
        p_age = input('Age: ')
        p_condition = input('Condition: ')
        p_status = input('Status: ')
        return cls(p_id, p_name, p_age, p_condition, p_status)




patient_list=[]
while True:
    print('Enter patient new details')
    new_patient = Patient.patient_details()
    patient_list.append(new_patient)
    more = input('Add another patient? (yes or no): ')
    if more.lower() != 'yes':
        break
    

print("\n" * 3)

print(f"{'ID':<5}| {'Name':<8}| {'Age':<3} | {'Condition':<15} | {'Status':<5}")
print("-"*50)
for patient in patient_list:
    print(f"{patient.id} | {patient.name:<7} | {patient.age:<3} | {patient.condition:<15} | {patient.status}")