# Statistical Testing Guide: T-test and F-test

## 1. Hypothesis Testing Basics
### Null Hypothesis (H0)
- States no significant difference exists
- Contains "equal to" (=)
- Default position we try to disprove

### Alternative Hypothesis (H1)
- States a difference exists
- Opposite of H0

## 2. T-Test
### Purpose
- Compares means of TWO groups
- Shows direction of difference
- Uses t-distribution

### Formula
```
t = (x̄ - μ) / (s/√n)    [One sample]
t = (x̄1 - x̄2) / √(s²/n1 + s²/n2)    [Two sample]

Where:
x̄ = sample mean
μ = population mean
s = standard deviation
n = sample size
```

### Sample Problem
**Problem:** Compare effectiveness of two painkillers
```
Data:
Painkiller A: n=10, x̄=3.5, s=1.2
Painkiller B: n=10, x̄=5.8, s=1.4

H0: μ1 = μ2
H1: μ1 ≠ μ2

t = (3.5 - 5.8) / √(1.2²/10 + 1.4²/10)
t = -3.945

Critical value = ±2.01
|-3.945| > 2.01
Result: Reject H0, Painkiller A more effective
```

## 3. F-Test
### Purpose
- Compares variance between 2+ groups
- Shows if differences exist (not direction)
- Uses F-distribution

### Formula
```
F = Variance between groups / Variance within groups
F = MSB / MSW

Where:
MSB = Mean Square Between groups
MSW = Mean Square Within groups
```

### Sample Problem
**Problem:** Compare three teaching methods
```
Data:
Method A: mean=85, SD=4, n=30
Method B: mean=78, SD=5, n=30
Method C: mean=82, SD=3, n=30

H0: μ1 = μ2 = μ3
H1: Not all means are equal

Calculate:
1. Total SS (Sum of Squares)
2. Between SS
3. Within SS
4. MSB and MSW
5. F = MSB/MSW

Compare with F-critical value
```

## 4. Key Differences

| Aspect | T-Test | F-Test |
|--------|---------|---------|
| Groups | Two only | Two or more |
| Direction | Shows direction | No direction |
| Distribution | t-distribution | F-distribution |
| Values | Positive/Negative | Only positive |
| Purpose | Mean comparison | Variance comparison |

## 5. Decision Rules

### T-Test
```
If |t| > critical value → Reject H0
If |t| < critical value → Accept H0
```

### F-Test
```
If F > critical value → Reject H0
If F < critical value → Accept H0
```

## 6. Common Critical Values
- T-test (α=0.05, df=29): ±2.045
- F-test (α=0.05):
  * df1=2, df2=87: 3.101
  * df1=3, df2=87: 2.711

## 7. Important Notes
1. Assumptions:
   - Normal distribution
   - Independent samples
   - Equal variances (for basic tests)

2. Sample Size:
   - Larger samples = More reliable results
   - Minimum recommended: 30 per group

3. Significance Level:
   - Typically α = 0.05 (95% confidence)
   - Can use α = 0.01 for stricter testing

4. Interpretation:
   - Consider practical significance
   - Look at effect size
   - Consider real-world implications
