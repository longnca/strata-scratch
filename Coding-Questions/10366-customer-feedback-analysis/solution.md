# Customer Feedback Analysis

- Interview Question Date: December 2023
- Capital One
- Medium
- ID 10366

## Question

Capital One's marketing team is working on a project to analyze customer feedback from their feedback surveys.


The team sorted the words from the feedback into three different categories;


•	short_comments
•	mid_length_comments
•	long_comments


The team wants to find comments that are not short and come from social media. The output should include 'feedback_id,' 'feedback_text,' 'source_channel,' and a calculated category.

## My solution

Here's my code:

SQL:

```sql
WITH filtered_comments AS (
	SELECT DISTINCT ON (feedback_id) feedback_id, feedback_text, source_channel, comment_category
	FROM customer_feedback
	WHERE source_channel = 'social_media' AND comment_category != 'short_comments'
	ORDER BY feedback_id, feedback_text, source_channel, comment_category
)
SELECT feedback_id, feedback_text, source_channel, comment_category
FROM filtered_comments
ORDER BY feedback_id;
```

Python:

```python
import pandas as pd 

# Filter the dataframe as per the requirements: not short_comments AND from social_media
filtered_df = customer_feedback[
    (customer_feedback['comment_category'] != 'short_comments') 
    & (customer_feedback['source_channel'] == 'social_media')]

# Update the dataframe with columns as required
filtered_df = filtered_df[['feedback_id', 'feedback_text', 'source_channel', 'comment_category']]

# Remove duplicates in the dataframe if any
filtered_df.drop_duplicates(inplace=True)

# Import the dataframe back to the original dataframe as required
customer_feedback = filtered_df

# Print the final dataframe
customer_feedback
```