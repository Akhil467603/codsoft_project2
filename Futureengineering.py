# One-Hot Encoding for categorical features like Genre, Director, Actors
encoder = OneHotEncoder(sparse=False)
encoded_features = encoder.fit_transform(df[['Genre', 'Director', 'Actors']])

# Convert to DataFrame
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out())

# Concatenate the encoded features with the original dataframe
df = pd.concat([df, encoded_df], axis=1)

# Drop the original categorical columns
df.drop(['Genre', 'Director', 'Actors'], axis=1, inplace=True)
