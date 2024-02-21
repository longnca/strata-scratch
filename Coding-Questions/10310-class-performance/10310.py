# Import your libraries
import pandas as pd

# Start writing code
box_scores.head()

# My solution

# Calculate the sum of assignement scores
box_scores['sum'] = box_scores['assignment1'] + box_scores['assignment2'] + box_scores['assignment3']

# Calculate the difference of max and min scores
diff_score = box_scores['sum'].max() - box_scores['sum'].min()