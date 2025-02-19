# Solutions for Machine Learning Questions 5-8

## 5. Gradient Boosting Deep Dive (20 marks)

a) Mathematical Foundation (8 marks)

1. Loss Function:
```
L(y, F(x)) = Σ(yᵢ - F(xᵢ))²  # For regression
L(y, F(x)) = -Σyᵢlog(p(yᵢ))  # For classification
```

2. Gradient Calculation:
```
Negative gradient: -[∂L/∂F(xᵢ)]
For squared loss: yᵢ - F(xᵢ)
```

3. Update Procedure:
```
F₍ₘ₎(x) = F₍ₘ₋₁₎(x) + γₘh₍ₘ₎(x)
where:
- F₍ₘ₎(x) is model at step m
- γₘ is step size
- h₍ₘ₎(x) is weak learner
```

b) Gradient Boost vs XGBoost (6 marks)

XGBoost Improvements:
1. Regularization:
   - L1 and L2 regularization
   - Shrinkage and column subsampling

2. System Optimization:
   - Cache-aware access
   - Parallel processing
   - Out-of-core computing

3. Algorithm Enhancements:
   - Approximate split finding
   - Handling missing values
   - Built-in tree pruning

c) Choosing XGBoost (3 marks)
- Large datasets
- Need for faster training
- Memory constraints
- When regularization is crucial
- Handling missing values important

d) XGBoost Regularization (3 marks)
```
Obj = Σ(L(yᵢ,ŷᵢ)) + Σ(Ω(fₖ))
where Ω(f) = γT + 1/2λ||w||²

- γ: complexity control
- T: number of leaves
- λ: L2 regularization
- w: leaf weights
```

## 6. MART and Advanced Tree Models (20 marks)

a) MART Characteristics (8 marks)

Tree Building Process:
1. Initial prediction: mean/median
2. Calculate residuals
3. Fit tree to residuals
4. Update predictions
5. Repeat with new residuals

Advantages:
- Natural handling of different types of predictors
- Automatic variable selection
- Captures non-linear relationships
- Handles missing values

b) MART Implementation (6 marks)

Splitting Criteria:
```
Improvement = MSE(parent) - (MSE(left) + MSE(right))
MSE = Σ(residual - mean_residual)²/N
```

Residual Usage:
```
1. Initial F₀(x) = ȳ
2. For m = 1 to M:
   - Compute residuals: rᵢₘ = yᵢ - F₍ₘ₋₁₎(xᵢ)
   - Fit tree to residuals
   - Update F₍ₘ₎(x) = F₍ₘ₋₁₎(x) + ν × tree_prediction
```

c) MART vs Random Forest (3 marks)
- Sequential vs Parallel
- Residual fitting vs Bootstrap sampling
- Stronger individual trees in RF
- MART better for additive relationships

d) MART Preference Scenarios (3 marks)
- Complex continuous relationships
- Need for interpretability
- High-dimensional data
- When variable interactions are important

## 7. Ensemble Method Comparison (20 marks)

a) Ensemble Solution Design (8 marks)

Voting Classifier:
```python
from sklearn.ensemble import VotingClassifier

# Base models
rf = RandomForestClassifier(class_weight='balanced')
xgb = XGBClassifier(scale_pos_weight=99)
lgbm = LGBMClassifier(is_unbalanced=True)

# Voting classifier
voting_clf = VotingClassifier(
    estimators=[('rf', rf), ('xgb', xgb), ('lgbm', lgbm)],
    voting='soft'
)
```

Stacking:
```python
from sklearn.ensemble import StackingClassifier

# Meta-learner
meta_learner = LogisticRegression()

# Stacking classifier
stacking_clf = StackingClassifier(
    estimators=[('rf', rf), ('xgb', xgb), ('lgbm', lgbm)],
    final_estimator=meta_learner,
    cv=5
)
```

b) Class Imbalance Handling (4 marks)
1. Data Level:
   - SMOTE
   - ADASYN
   - Random under-sampling

2. Algorithm Level:
   - Class weights
   - Focal loss
   - Custom evaluation metrics

c) Computational Comparison (4 marks)
```
Method          Training Time    Prediction Time    Memory Usage
Random Forest   Medium          Fast              High
XGBoost        Medium          Fast              Medium
Stacking       High            Medium            High
Voting         Medium          Medium            Medium
```

d) Recommendations (4 marks)
1. Use Stacking with:
   - SMOTE preprocessing
   - Cross-validation for meta-learner
   - Diverse base models
2. Monitor with:
   - Precision-Recall curve
   - AUROC
   - F1-score

## 8. Practical Implementation (20 marks)

a) Optimization Strategy (8 marks)

Feature Selection:
```python
from sklearn.feature_selection import SelectFromModel

# Use L1-based selection
selector = SelectFromModel(
    estimator=LGBMClassifier(),
    max_features=50
)

X_selected = selector.fit_transform(X, y)
```

Hyperparameter Tuning:
```python
from sklearn.model_selection import RandomizedSearchCV

param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

random_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_dist,
    n_iter=20,
    cv=3,
    n_jobs=-1
)
```

b) Cross-validation Implementation (4 marks)
```python
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import make_scorer, f1_score

skf = StratifiedKFold(n_splits=5, shuffle=True)
scorer = make_scorer(f1_score, average='weighted')

scores = cross_val_score(
    estimator=model,
    X=X_selected,
    y=y,
    cv=skf,
    scoring=scorer,
    n_jobs=-1
)
```

c) Memory Management (4 marks)
1. Use disk-based processing
2. Implement batch processing
3. Use sparse matrices
4. Feature selection before training
5. Memory-efficient algorithms

d) Model Complexity Trade-offs (4 marks)
1. Performance vs Training Time:
   - More trees = better performance but slower training
   - Deeper trees = better fit but more memory

2. Memory vs Accuracy:
   - Feature selection might reduce accuracy
   - Batch processing might affect convergence

3. Recommendations:
   - Start simple, increase complexity as needed
   - Monitor validation metrics
   - Use early stopping
