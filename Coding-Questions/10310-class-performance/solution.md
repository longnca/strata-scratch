# Class Performance

- Interview Question Date: December 2020
- Box
- Easy
- ID: 10310

## Question

You are given a table containing assignment scores of students in a class. Write a query that identifies the largest difference in total score  of all assignments.

Output just the difference in total score (sum of all 3 assignments) between a student with the highest score and a student with the lowest score.

## My solution

Here's how I solved this question:

- Calculate the sum of each student's scores by summarizing the Assignment 1, 2, and 3. Call this new column 'sum'.
- Find the max and min of this column 'sum'.
- Calculate the difference between max and min values.

Here's my code:

```python
# Import your libraries
import pandas as pd

# Start writing code
box_scores.head()

# My solution

# Calculate the sum of assignement scores
box_scores['sum'] = box_scores['assignment1'] + box_scores['assignment2'] + box_scores['assignment3']

# Calculate the difference of max and min scores
diff_score = box_scores['sum'].max() - box_scores['sum'].min()
```