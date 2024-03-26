# My solution steps:
# Find the user ID for Karl and Hans
# Find friends of Karl and Hans separately
# Find mutual friends' IDs
# Get mutual friends' names

# Import your libraries
import pandas as pd

# Start writing code
users.head()

# Find the user ID for Karl and Hans separately
karl_id = users[users['user_name']=="Karl"].iloc[0][0]
hans_id = users[users['user_name']=="Hans"].iloc[0][0]

# Find friends of Karl and Hans
karl_friends = friends[friends['user_id']==karl_id]
hans_friends = friends[friends['user_id']==hans_id]

# Find mutual friends' ID
mutual_friend_ids = karl_friends.merge(hans_friends, how='inner', on='friend_id').iloc[0][1]

# Get mutual friends' names
mutual_friend_names = users[users['user_id']==mutual_friend_ids]

# Print mutual friends' names
mutual_friend_names


# COMPARE WITH STRATASCRATCH'S SOLUTION BELOW

import pandas as pd

# Find the user IDs for Karl and Hans
karl_id = users[users['user_name'] == 'Karl']['user_id'].iloc[0]
hans_id = users[users['user_name'] == 'Hans']['user_id'].iloc[0]

# Find friends of Karl and Hans
karl_friends = friends[friends['user_id'] == karl_id]['friend_id'].tolist()
hans_friends = friends[friends['user_id'] == hans_id]['friend_id'].tolist()

# Find mutual friends' IDs
mutual_friends_ids = list(set(karl_friends).intersection(hans_friends))

# Get mutual friends' user names
mutual_friends = users[users['user_id'].isin(mutual_friends_ids)]

mutual_friends