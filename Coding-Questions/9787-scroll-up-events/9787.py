# Find all users that have performed at least one `scroll_up` event.

# Import your libraries
import pandas as pd

# Start writing code
facebook_web_log.head()

# Find user_id that have at least one 'scroll_up' event
facebook_web_log[facebook_web_log['action']=='scroll_up'][['user_id']].drop_duplicates()