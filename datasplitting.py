# Split the data into features and target
X = df.drop('Rating', axis=1)  # Features
y = df['Rating']               # Target (Rating)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
