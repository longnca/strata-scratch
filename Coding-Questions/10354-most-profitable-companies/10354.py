"""My solution"""

# Import library
import pandas as pd

# Check the dataframe
forbes_global_2010_2014.head()

# Find the top 3 most profitable companies in the dataset
df_top3 = forbes_global_2010_2014.nlargest(3, "profits")

# Select and display only the 'company' and 'profits' columns
df_top3[["company", "profits"]]


"""Alternative solution"""

# Import library
import pandas as pd

# Check the dataframe
forbes_global_2010_2014.head()

# Sort the dataframe based on 'profits'
sorted_df = forbes_global_2010_2014.sort_values(by="profits", ascending=False)

# Filter top 3 rows
sorted_df.head(3)

# Show results
sorted_df.head(3)[["company", "profits"]]