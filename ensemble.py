import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_curve, auc
import matplotlib.pyplot as plt

# Load the iris dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a decision tree classifier
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)
dt_predictions = decision_tree.predict(X_test)

# Build a random forest classifier
random_forest = RandomForestClassifier()
random_forest.fit(X_train, y_train)
rf_predictions = random_forest.predict(X_test)

# Build a bagging classifier
bagging = BaggingClassifier()
bagging.fit(X_train, y_train)
bagging_predictions = bagging.predict(X_test)

# Build a boosting classifier
boosting = AdaBoostClassifier()
boosting.fit(X_train, y_train)
boosting_predictions = boosting.predict(X_test)

# Build a voting classifier with soft voting
voting = VotingClassifier(
    estimators=[('dt', decision_tree), ('rf', random_forest), ('bagging', bagging), ('boosting', boosting)],
    voting='soft'
)
voting.fit(X_train, y_train)
voting_predictions = voting.predict(X_test)

# Compare the performance of different classifiers
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_predictions))
print("Random Forest Accuracy:", accuracy_score(y_test, rf_predictions))
print("Bagging Accuracy:", accuracy_score(y_test, bagging_predictions))
print("Boosting Accuracy:", accuracy_score(y_test, boosting_predictions))
print("Voting Accuracy:", accuracy_score(y_test, voting_predictions))

# Plot the ROC curve for each classifier using subplots
classifiers = {
    'Decision Tree': decision_tree,
    'Random Forest': random_forest,
    'Bagging': bagging,
    'Boosting': boosting,
    'Voting': voting
}

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

for ax, (name, classifier) in zip(axes.flat, classifiers.items()):
    if name != 'Voting':
        y_score = classifier.predict_proba(X_test)
        fpr, tpr, _ = roc_curve(y_test, y_score[:, 1], pos_label=1)
        roc_auc = auc(fpr, tpr)
        ax.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.2f})')
        ax.plot([0, 1], [0, 1], 'k--')  # Diagonal line for random classifier
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title(f'{name} - ROC Curve')
        ax.legend(loc='lower right')

plt.tight_layout()
plt.show()
