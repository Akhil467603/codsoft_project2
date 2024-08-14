# Check for missing values
df.isnull().sum()

# Handle missing values
df.fillna('', inplace=True)  # Fill missing strings with empty strings

# Drop irrelevant columns (if any)
df.drop(['MovieID', 'Title'], axis=1, inplace=True)  # Example columns to drop
