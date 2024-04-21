# Patient Management System

This project serves as part of the Computer Programmer I Examination for Baguio General Hospital and Medical Center.

## Features

- **Display Patients**: View a list of patients including their name, date of birth, and address.
- **Add Patient**: Add a new patient to the system by providing their name, date of birth, and address.
- **Update Patient**: Modify existing patient information such as name, date of birth, and address.
- **Delete Patient**: Remove a patient from the system.
- **Admission Management**: Manage patient admissions, including fetching current admissions, admitting new patients, and discharging patients.

## How It Works

The Patient Management System is implemented using the Tkinter library in Python. Here's a breakdown of how the code works:

1. **Main Window**: The main window displays a list of patients and provides buttons for managing patients and admissions.

2. **Patient Management**:
   - `display_patients()`: Retrieves patient data and displays it in a text widget.
   - `add_patient()`: Allows the user to input data for a new patient and adds them to the system.
   - `update_patient()`: Enables updating existing patient information.
   - `delete_patient()`: Removes a patient from the system.
   
3. **Admission Management**:
   - `open_admission_ui()`: Opens a separate window for admission management, displaying current admissions and providing options to fetch, admit, and discharge patients.
   - Placeholder functions (`fetch_admissions()`, `admit_patient()`, `discharge_patient()`) are included for managing admissions.

## Getting Started

To run the Patient Management System:
1. Ensure to have Python installed on your system.
2. Clone this repository.
3. Navigate to the project directory in terminal.
4. Run the `patient_management.py` file using Python.



- Sophia Nicole Garcia
