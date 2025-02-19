# Machine Learning Questions (20 marks each)

1. Decision Tree Fundamentals (20 marks)
   Given the following dataset about loan approval:
   ```
   Income  Credit_Score  Existing_Loan  Approval
   High    Good         No             Yes
   Low     Poor         Yes            No
   Medium  Good         No             Yes
   High    Poor         No             Yes
   Low     Good         Yes            No
   ```
   a) Construct a decision tree using Entropy as the impurity measure. Show all calculations for the root node split. (8 marks)
   b) Calculate the Gini index for the same root node split and compare with entropy results. (6 marks)
   c) Explain how the inductive bias in decision trees would affect this model. (3 marks)
   d) Discuss potential issues with decision tree learning for this dataset. (3 marks)

2. CART Analysis (20 marks)
   Consider a regression problem predicting house prices with features: size, location, age, and rooms.
   a) Explain the key differences between classification and regression trees. (5 marks)
   b) Given a node with values [200K, 220K, 250K, 300K, 350K]:
      - Calculate the mean squared error
      - Explain how CART would make a split decision
      Show all calculations. (8 marks)
   c) Describe pruning techniques in CART and wc:\Users\DeepanShanmugam\Downloads\ml-answers-5-8.md c:\Users\DeepanShanmugam\Downloads\ml-answers-1-4.mdhen to use them. (4 marks)
   d) How would you handle missing values in this dataset using CART? (3 marks)

3. Random Forest Implementation (20 marks)
   ```python
   from sklearn.ensemble import RandomForestClassifier
   import pandas as pd

   # Given dataset
   data = pd.read_csv('customer_churn.csv')
   ```
   a) Write code to:
      - Implement Random Forest with bootstrapping
      - Set appropriate hyperparameters
      - Handle class imbalance
      Include comments explaining your choices. (8 marks)
   b) Explain how bootstrapping works in Random Forest and its importance. (4 marks)
   c) How would you determine the optimal number of trees and maximum depth? (4 marks)
   d) Describe methods to handle the minority class problem in this context. (4 marks)

4. AdaBoost Analysis (20 marks)
   a) Given the following weak learner results on a binary classification problem:
   ```
   Iteration  Sample_Weights  Error_Rate  Alpha
   1         [0.2,0.2,...]   0.3         ?
   2         [0.25,0.15...]. 0.25        ?
   3         [0.3,0.1,...]   0.2         ?
   ```
   Calculate:
   - Alpha values for each iteration
   - Updated sample weights
   Show all steps. (10 marks)
   b) Explain how AdaBoost combines weak learners to create a strong learner. (5 marks)
   c) Compare AdaBoost's approach to handling errors with Random Forest's approach. (5 marks)

5. Gradient Boosting Deep Dive (20 marks)
   a) Explain the mathematical foundation of Gradient Boosting, including:
      - Loss function
      - Gradient calculation
      - Update procedure
      (8 marks)
   b) Compare and contrast:
      - Gradient Boost vs XGBoost
      - Key improvements in XGBoost
      (6 marks)
   c) When would you choose XGBoost over basic Gradient Boosting? (3 marks)
   d) Explain regularization in XGBoost and its importance. (3 marks)

6. MART and Advanced Tree Models (20 marks)
   a) Explain how MART differs from traditional regression trees. Include:
      - Tree building process
      - Handling of variables
      - Advantage over single trees
      (8 marks)
   b) Given a regression problem:
      - Describe MART's splitting criteria
      - Show how residuals are used
      Use examples. (6 marks)
   c) Compare MART with Random Forest for regression tasks. (3 marks)
   d) Discuss scenarios where MART would be preferred over other tree-based methods. (3 marks)

7. Ensemble Method Comparison (20 marks)
   Given a credit card fraud detection problem with 1% fraud cases:
   a) Design an ensemble solution using:
      - Voting classifier
      - Stacking
      Explain your choice of base models and architecture. (8 marks)
   b) How would you handle the severe class imbalance in this case? (4 marks)
   c) Compare the computational costs and performance tradeoffs of different ensemble methods. (4 marks)
   d) Recommend the best ensemble approach for this problem with justification. (4 marks)

8. Practical Implementation and Optimization (20 marks)
   Given a large dataset (1M rows) with 100 features:
   ```python
   # Sample code structure
   from sklearn.ensemble import (RandomForestClassifier, 
                               GradientBoostingClassifier,
                               VotingClassifier)
   ```
   a) Develop an optimization strategy for:
      - Feature selection
      - Hyperparameter tuning
      - Model selection
      Include code snippets. (8 marks)
   b) Implement cross-validation with appropriate metrics. Explain your choices. (4 marks)
   c) How would you handle memory constraints while training these models? (4 marks)
   d) Discuss the tradeoff between model complexity and performance. (4 marks)

Note: Each question requires:
- Clear explanation of concepts
- Proper mathematical notation where needed
- Code examples where appropriate
- Practical considerations
- Performance implications
