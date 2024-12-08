from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import numpy as np

# Generate a sample dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Initialize Logistic Regression model
model = LogisticRegression(max_iter=10000)

# Perform 5-Fold Cross-Validation and get accuracy for each fold
accuracy_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

# Display each fold's accuracy and the mean accuracy
print("Accuracy for each fold:", accuracy_scores)
print("Average Accuracy:", np.mean(accuracy_scores))
