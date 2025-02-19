# Machine Learning Questions (20 marks each)

1. Decision Tree Construction (20 marks)
   Given the following dataset:
   ```
   Size(sq ft)  Age   Rooms   Class
   1500         15    2       budget
   1800         10    3       medium
   2000         8     3       medium
   2500         5     4       luxury
   3000         2     5       luxury
   ```
   a) Calculate Gini impurity for each possible split on each feature. Show all calculations. (8 marks)
   b) Identify the best split and justify your choice using Weighted Gini calculations. (6 marks)
   c) After the first split, calculate the next best split for the largest child node. (6 marks)

2. CART Analysis (20 marks)
   Consider the housing dataset:
   ```
   Size(sq ft)  Price($K)
   1200         200
   1500         250
   1800         280
   2000         300
   2200         320
   2500         350
   2800         380
   3000         400
   ```
   a) Explain with calculations how CART would:
      - Choose split points
      - Calculate MSE for each split
      - Select best split (8 marks)
   b) Compare this with classification tree splitting criteria (6 marks)
   c) Explain how pruning would work on this regression tree (6 marks)

3. Random Forest Implementation (20 marks)
   Given this dataset:
   ```
   Age  Income  Credit_Score  Default
   25   30K     650          No
   35   45K     700          No
   45   35K     680          Yes
   28   25K     600          Yes
   50   60K     750          No
   ```
   a) Show how bootstrapping would create different training sets (6 marks)
   b) Demonstrate feature randomization at each split (6 marks)
   c) Explain the voting process with calculations (4 marks)
   d) Handle class imbalance in this dataset (4 marks)

4. AdaBoost Analysis (20 marks)
   Using the same dataset as Question 3:
   a) Calculate for first three iterations:
      - Sample weights
      - Error rates
      - Alpha values
   Show all calculations. (10 marks)
   b) Update weights for misclassified samples (5 marks)
   c) Calculate final predictions (5 marks)

5. Gradient Boosting Deep Dive (20 marks)
   Given regression dataset:
   ```
   X  Y
   1  2.1
   2  4.2
   3  5.8
   4  8.1
   5  9.6
   ```
   a) Calculate initial prediction (average) (4 marks)
   b) Calculate residuals (4 marks)
   c) Show how to fit a tree to residuals (6 marks)
   d) Calculate predictions after first iteration (6 marks)

6. Comparing Ensemble Methods (20 marks)
   Using this classification dataset:
   ```
   Feature1  Feature2  Feature3  Class  
   5         2         High      A
   3         4         Low       B
   6         1         High      A
   2         5         Low       B
   4         3         Medium    A
   ```
   Compare three models with calculations:
   a) Random Forest (7 marks)
   b) AdaBoost (7 marks)
   c) Gradient Boosting (6 marks)

7. MART and XGBoost (20 marks)
   Given a time series dataset of daily sales:
   ```
   Day  Sales  Temperature  Weekend
   1    100    25          No
   2    150    28          No
   3    200    30          Yes
   4    180    29          Yes
   5    120    26          No
   ```
   a) Apply MART algorithm (8 marks)
   b) Show XGBoost improvements (6 marks)
   c) Handle missing values (6 marks)

8. Practical Implementation and Tuning (20 marks)
   For a credit card fraud detection problem:
   ```
   Amount  Time  V1    V2    Fraudulent
   100     0     0.1   0.2   No
   2000    1     1.2   -0.3  Yes
   150     2     0.3   0.1   No
   3000    3     -1.0  -0.8  Yes
   50      4     0.2   0.3   No
   ```
   a) Design and justify ensemble approach (6 marks)
   b) Handle imbalanced classes (6 marks)
   c) Select and tune hyperparameters (4 marks)
   d) Evaluate model performance (4 marks)

Note for all questions:
- Show all calculations clearly
- Explain your reasoning at each step
- Include formulas before calculations
- Consider practical implications
