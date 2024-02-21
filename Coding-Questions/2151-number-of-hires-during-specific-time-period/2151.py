# Import your libraries
import pandas as pd

# Start writing code
employees.head()

# My solution

# Filter the dataframe based on the date range condition
df = employees[(employees.joining_date >= '2022-01-01') & (employees.joining_date <= '2022-07-31')]

# Optional: check the dataframe after filtering
df.head()

# Count the number of employees in this new dataframe
df['id'].count()

# returns: 3 - Correct!