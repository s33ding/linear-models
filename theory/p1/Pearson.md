# Pearson Correlation Coefficient

<iframe width="560" height="315" src="https://www.youtube.com/embed/xZ_z8KWkhXE?si=kFtZtQZfPgxaWF35" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Definition

The Pearson correlation coefficient measures the **linear relationship** between two continuous variables. It assumes **bivariate normality** (variables are jointly normally distributed) and is **sensitive to outliers**. The coefficient is denoted as **r**.

## Formula

![[pearson.png]]

where xi and yi are data points, and x̄ and ȳ are their respective means.

## Key Properties

- **Range:** Always between -1 and +1
- **Perfect positive correlation:** r = 1
- **Perfect negative correlation:** r = -1  
- **No linear relationship:** r = 0

## Python Implementation

```python
import numpy as np
from scipy.stats import pearsonr

# Temperature data in Celsius and corresponding Fahrenheit
temperature_celsius = np.array([0, 10, 20, 30, 40])
temperature_fahrenheit = np.array([32, 50, 68, 86, 104])  # Converted from Celsius

# Calculate Pearson correlation coefficient
correlation_coefficient, p_value = pearsonr(temperature_celsius, temperature_fahrenheit)
print("Pearson correlation coefficient:", correlation_coefficient)
```

**Output:** Pearson correlation coefficient: 1.0

The output shows a perfect positive linear relationship (r = 1.0) since Fahrenheit = 1.8 × Celsius + 32.

## Correlation vs. Covariance

- **Covariance** indicates direction but depends on units, making comparison difficult
- **Correlation** standardizes covariance by dividing by standard deviations, producing a unitless value between -1 and 1
