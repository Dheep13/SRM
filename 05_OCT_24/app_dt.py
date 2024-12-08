# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

# Create the dataset
data = {'Age': ['<=30', '<=30', '<=30', '31-40', '>40', '>40', '>40', '<=30'],
        'Income': ['Low', 'Medium', 'High', 'Medium', 'Low', 'High', 'Medium', 'Medium'],
        'BuysCar': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']}

df = pd.DataFrame(data)

# Convert categorical variables into numerical ones (one-hot encoding)
df = pd.get_dummies(df, columns=['Age', 'Income'])

# Separate features (X) and target (y)
X = df.drop('BuysCar', axis=1)
y = df['BuysCar'].apply(lambda x: 1 if x == 'Yes' else 0)  # Convert 'Yes' to 1 and 'No' to 0

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

import matplotlib.pyplot as plt
from sklearn import tree

# Adjust the figure size and tree parameters
plt.figure(figsize=(20,10))  # Increase the figure size for better readability

# Plot the decision tree with more customization
tree.plot_tree(clf, 
               feature_names=X.columns,  # Feature names
               class_names=['No', 'Yes'],  # Class names
               filled=True,  # Fill colors for the nodes
               rounded=True,  # Rounded corners for nodes
               proportion=True,  # Show proportion of samples in each node
               fontsize=12)  # Increase font size for better readability

plt.show()



# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
