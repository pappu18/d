import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('weather.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('play', axis=1), df['play'], test_size=0.3, random_state=42)

# Get the feature names
feature_names = X_train.columns

# Create a Naive Bayes model
nb = GaussianNB()

# Train the model using the training set
nb.fit(X_train, y_train)

# Rename the feature names with their original names
nb.classes_ = df['play'].unique()
nb.theta_ = nb.theta_[:, :-1]
nb.sigma_ = nb.sigma_[:, :-1]
nb.epsilon_ = 1e-9
nb.class_count_ = y_train.value_counts().sort_index().values
nb.n_features_ = len(feature_names)

# Test the model using the testing set
y_pred = nb.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
