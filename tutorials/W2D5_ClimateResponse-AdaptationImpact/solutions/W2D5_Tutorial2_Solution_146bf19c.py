
# Display a histogram of the Pandas DataFrame 'df'
df_features.hist(figsize=[20,20])

# Output the sum of null values for each column in 'df'
df_features.isnull().sum()