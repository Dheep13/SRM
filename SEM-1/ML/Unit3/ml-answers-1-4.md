# Solutions for Machine Learning Questions 1-4

## 1. Decision Tree Fundamentals (20 marks)

a) Entropy Calculations for Root Node Split (8 marks)

Step 1: Calculate total entropy
```
Total examples = 5
P(Yes) = 3/5, P(No) = 2/5
Entropy = -3/5 log₂(3/5) - 2/5 log₂(2/5) = 0.971 bits
```

For Income split:
```
High (2 examples): P(Yes)=2/2, P(No)=0/2
  Entropy = 0 bits
Medium (1 example): P(Yes)=1/1, P(No)=0/1
  Entropy = 0 bits
Low (2 examples): P(Yes)=0/2, P(No)=2/2
  Entropy = 0 bits

Information Gain = 0.971 - (2/5×0 + 1/5×0 + 2/5×0) = 0.971
```

b) Gini Index Calculations (6 marks)

For total dataset:
```
Gini = 1 - (3/5)² - (2/5)² = 0.48

For Income split:
High: 1 - (1)² - (0)² = 0
Medium: 1 - (1)² - (0)² = 0
Low: 1 - (0)² - (1)² = 0

Weighted Gini = (2/5×0 + 1/5×0 + 2/5×0) = 0
Gini Gain = 0.48 - 0 = 0.48
```

c) Inductive Bias Discussion (3 marks)
- Prefers shorter trees (Occam's Razor)
- Favors attributes with more distinct values
- Assumes classes are separable by axis-parallel boundaries
- May overfit with small datasets

d) Potential Issues (3 marks)
- Small dataset size leading to overfitting
- Limited feature set
- Potential noise in Credit_Score assessment
- Binary splits might not capture complex relationships

## 2. CART Analysis (20 marks)

a) Classification vs Regression Trees (5 marks)
1. Split Criteria:
   - Classification: Gini index/Entropy
   - Regression: Mean Squared Error/MAE

2. Leaf Values:
   - Classification: Most common class
   - Regression: Mean/median of samples

3. Error Measurement:
   - Classification: Misclassification rate
   - Regression: Squared/absolute error

b) MSE Calculations (8 marks)
```
Mean = (200K + 220K + 250K + 300K + 350K)/5 = 264K

MSE = Σ(x - mean)²/n
    = [(200-264)² + (220-264)² + (250-264)² + (300-264)² + (350-264)²]/5
    = 3,432,800

For split decision:
- Consider each possible split point
- Calculate weighted MSE for resulting groups
- Choose split minimizing weighted MSE
```

c) Pruning Techniques (4 marks)
1. Pre-pruning:
   - Minimum samples per leaf
   - Maximum depth
   - Maximum features

2. Post-pruning:
   - Cost complexity pruning
   - Reduced error pruning
   Use when: Overfitting detected via validation set

d) Handling Missing Values (3 marks)
1. Surrogate splits
2. Imputation at nodes
3. Majority direction
Best practice: Use surrogate splits for CART

## 3. Random Forest Implementation (20 marks)

a) Implementation Code (8 marks)
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# Handle imbalance
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Initialize Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',
    bootstrap=True,
    class_weight='balanced',
    random_state=42
)

# Train model
rf.fit(X_resampled, y_resampled)
```

b) Bootstrapping Explanation (4 marks)
- Each tree gets random sample with replacement
- ~63.2% unique samples per tree
- Remaining samples form OOB (Out-of-Bag) set
- Increases model diversity and reduces overfitting

c) Optimal Parameters (4 marks)
1. Number of trees:
   - Plot OOB error vs n_estimators
   - Choose point where error stabilizes
   
2. Maximum depth:
   - Use cross-validation
   - Monitor validation error
   - Stop when validation error increases

d) Handling Minority Class (4 marks)
1. Class weights
2. SMOTE/ADASYN
3. Balanced random forest
4. Adjusting threshold
5. Combine with boosting

## 4. AdaBoost Analysis (20 marks)

a) Calculations (10 marks)

For iteration 1:
```
Error rate = 0.3
α₁ = 0.5 × ln((1-0.3)/0.3) = 0.847

Updated weights:
- Correct predictions: w × e^(-0.847)
- Incorrect predictions: w × e^(0.847)
```

For iteration 2:
```
Error rate = 0.25
α₂ = 0.5 × ln((1-0.25)/0.25) = 1.099

Updated weights similarly
```

For iteration 3:
```
Error rate = 0.2
α₃ = 0.5 × ln((1-0.2)/0.2) = 1.386
```

b) Weak to Strong Learner (5 marks)
1. Weighted majority voting
2. Final prediction: sign(Σαᵢhᵢ(x))
3. Each weak learner contributes proportional to accuracy
4. Sequential learning focuses on hard examples
5. Theoretical guarantee of error reduction

c) AdaBoost vs Random Forest (5 marks)

AdaBoost:
- Sequential learning
- Weighted samples
- Focus on hard cases
- More sensitive to noise

Random Forest:
- Parallel learning
- Equal sample weights
- Random subsets
- More robust to noise
