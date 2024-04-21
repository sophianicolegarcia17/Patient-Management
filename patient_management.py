import tkinter as tk
from tkinter import font
from tkinter import messagebox

# Sample data
patients = [
    {"name": "Juan Dela Cruz", "dob": "01/01/1990", "address": "123 Session St"},
    {"name": "Maria Clara", "dob": "05/10/1985", "address": "456 Bakakeng St"}
]

admissions = [
    {"patient": "Juan Dela Cruz", "admission_date": "2024-04-21", "ward": "A"},
    {"patient": "Maria Clara", "admission_date": "2024-04-22", "ward": "B"}
]

# functions
def display_patients():
    patient_text.delete(1.0, tk.END)  # Clear previous text
    for patient in patients:
        patient_text.insert(tk.END, f"Name: {patient['name']}\nDOB: {patient['dob']}\nAddress: {patient['address']}\n\n")

def add_patient():
    # Get input from the user
    name = input("Enter patient's name: ")
    dob = input("Enter patient's date of birth (MM/DD/YYYY): ")
    address = input("Enter patient's address: ")

    # Create a new patient dictionary
    new_patient = {"name": name, "dob": dob, "address": address}

    # Add the new patient to the patients list
    patients.append(new_patient)

    print("Added a new patient:", new_patient)
    display_patients()  # Update display

def update_patient():
    name_to_update = input("Enter the name of the patient to update: ")
    for patient in patients:
        if patient["name"] == name_to_update:
            new_name = input("Enter the new name: ")
            new_dob = input("Enter the new date of birth (MM/DD/YYYY): ")
            new_address = input("Enter the new address: ")

            # Update the patient's information
            patient["name"] = new_name
            patient["dob"] = new_dob
            patient["address"] = new_address

            print("Updated the patient:", patient)
            display_patients()  # Update display
            return

    print("Patient not found")


def delete_patient():
    name_to_delete = input("Enter the name of the patient to delete: ")
    for patient in patients:
        if patient["name"] == name_to_delete:
            patients.remove(patient)
            print("Deleted the patient:", patient)
            display_patients()  # Update display
            return

    print("Patient not found")

def fetch_admissions():
    # Placeholder function for fetching and displaying admissions
    messagebox.showinfo("Admissions", "Fetching and displaying admissions within the current day")

def admit_patient():
    # Placeholder function for admitting a patient
    messagebox.showinfo("Admit Patient", "Admitting a patient")

def discharge_patient():
    # Placeholder function for discharging a patient
    messagebox.showinfo("Discharge Patient", "Discharging a patient")

def open_admission_ui():
    admission_window = tk.Toplevel(root)
    admission_window.title("Admission Management")

    admission_text = tk.Text(admission_window, width=40, height=10, font=custom_font)
    admission_text.pack(pady=10)

    admission_text.delete(1.0, tk.END)  # Clear previous text
    for admission in admissions:
        admission_text.insert(tk.END,
                               f"Patient: {admission['patient']}\nAdmission Date: {admission['admission_date']}\nWard: {admission['ward']}\n\n")

    # Buttons for admission management
    fetch_button = tk.Button(admission_window, text="Fetch Admissions", command=fetch_admissions, font=custom_font)
    fetch_button.pack(pady=5)
    admit_button = tk.Button(admission_window, text="Admit Patient", command=admit_patient, font=custom_font)
    admit_button.pack(pady=5)
    discharge_button = tk.Button(admission_window, text="Discharge Patient", command=discharge_patient, font=custom_font)
    discharge_button.pack(pady=5)

# Main window
root = tk.Tk()
root.title("Patient Management")

custom_font = font.Font(family="Helvetica", size=12)
root.configure(bg='#FFCCCC')

# Text widget to display patients
patient_text = tk.Text(root, width=40, height=20, font=custom_font)
patient_text.pack(pady=10)

# Buttons for patient management
add_button = tk.Button(root, text="Add Patient", command=add_patient, font=custom_font)
add_button.pack(pady=5)
update_button = tk.Button(root, text="Update Patient", command=update_patient, font=custom_font)
update_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Patient", command=delete_patient, font=custom_font)
delete_button.pack(pady=5)

# Button for admission management
admission_button = tk.Button(root, text="Admission Management", command=open_admission_ui, font=custom_font)
admission_button.pack(pady=5)

# Display initial patient list
display_patients()

root.mainloop()
