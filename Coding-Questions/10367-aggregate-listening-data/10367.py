# Import your libraries
import pandas as pd

# Fill the missing values with 0 before arithmetic operations
listening_habits['listen_duration'].fillna(0)

# Aggregation functions 
data = listening_habits.groupby(by='user_id').agg(total_listen_duration=('listen_duration', 'sum'), unique_song_count=('song_id', 'nunique')).reset_index()

# Rounding total_listen_duration to the nearest minute
data['total_listen_duration'] = (data['total_listen_duration']/60).round()

data