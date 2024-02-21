# Number of Hires During Specific Time Period

- Interview Question Date: February 2023
- Deloitte
- Easy
- ID: 2151

## Question

You have been asked to find the number of employees hired between the months of January and July in the year 2022 inclusive.

Your output should contain the number of employees hired in this given time frame.

## My solution

Here's how I solved this question:

- Analyze the problem: focus on the filtering condition of date range between 2022-01-01 to 2022-07-31 (inclusive).
- I'll have to filter the dataframe with the column 'joining_date' having the condition above.
- After filtering the dataframe, I'll count the number of unique records using `.count()` method of pandas. I'll choose the column 'id' assuming this is the unique id for each employee and record in the dataframe.

Here's my code:

```python
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
```