import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate a sample dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Create a DataFrame for easier viewing
df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(20)])
df['target'] = y

# Print the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())
print("\nShape of X:", X.shape)
print("Shape of y:", y.shape)

# Rest of the code remains the same...
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)
KFold()
accuracy_scores = []

for fold, (train_index, val_index) in enumerate(kf.split(X), 1):
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y[train_index], y[val_index]
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    accuracy_scores.append(accuracy)
    
    print(f"Fold {fold} Accuracy: {accuracy:.4f}")

average_accuracy = np.mean(accuracy_scores)
print(f"\nAverage Accuracy: {average_accuracy:.4f}")