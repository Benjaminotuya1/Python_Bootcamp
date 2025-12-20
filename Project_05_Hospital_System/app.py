import streamlit as st
from hospital_backend import Hospital, Patient, Doctor

# 1. Create the Hospital in the App
# We need to create the instance here so the app can use it
st_hospital = Hospital('St. Benjamin Streamlit Hospital')

# 2. Hire a Doctor (Hardcoded for now, so the AI works)
dr_ben = Doctor('Benjamin', 45, 'Neurosurgeon')
dr_chi = Doctor('chidi', 45, 'General Doctor')
dr_mat = Doctor('matthew', 45, 'Resident doctor')
dr_frk = Doctor('Frank', 45, 'orthoprdic surgion')

st_hospital.hire_doctor(dr_ben)
st_hospital.hire_doctor(dr_chi)
st_hospital.hire_doctor(dr_mat)
st_hospital.hire_doctor(dr_frk)


# 3. The Title
st.title("🏥 AI Telemedicine Terminal")
st.write("Welcome to the automated triage system.")

