# Aggregate Listening Data

- Interview Question Date: December 2023
- Spotify
- Easy
- ID 10367

## Question

You're tasked with analyzing a Spotify-like dataset that captures user listening habits.
For each user, calculate the total listening time and the count of unique songs they've listened to. Round the total listening duration to the nearest whole minute.


The output should contain three columns: 'user_id', 'total_listen_duration', and 'unique_song_count'.

## My solution

Here's my code:

```sql
SELECT 
	ROUND(SUM(COALESCE(listen_duration,0)/60.0)) AS total_listen_duration,
	COUNT(DISTINCT(song_id)) AS unique_song
FROM listening_habits
GROUP BY user_id;
```