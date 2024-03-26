# SOLUTION 1 
no_overtime = sf_public_salaries[sf_public_salaries['overtimepay']==0]['jobtitle']
pd.unique(no_overtime)

# SOLUTION 2 - method chaining
result = sf_public_salaries[sf_public_salaries['overtimepay'] == 0.0][['jobtitle']].drop_duplicates()
