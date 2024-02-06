# Import your libraries
import pandas as pd

# Check out the dataframe
employee_list.head()

# Create a dataframe of Johnson/Doctor
johnson_doctor = employee_list[(employee_list['profession'] == "Doctor") & (employee_list['last_name'] == "Johnson")]

# Show the final dataframe
johnson_doctor[['first_name', 'last_name']]