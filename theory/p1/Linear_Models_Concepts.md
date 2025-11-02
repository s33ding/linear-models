# Linear Models Theory - Part 1

## Matrix Concepts

### Matriz Identidade (Identity Matrix)

A **matriz identidade** In é uma matriz quadrada onde todos os elementos da **diagonal principal** são 1 e todos os outros elementos são 0.

Conceitualmente, a matriz identidade é o **elemento neutro da multiplicação de matrizes**, ou seja, qualquer matriz AAA multiplicada por III permanece **inalterada**:

### Matriz Determinante (Determinant)

O **determinante** é um número associado a uma matriz quadrada que resume algumas de suas propriedades essenciais. Ele indica, por exemplo:

- Se a matriz é **invertível** (uma matriz é invertível se seu determinante for diferente de zero).
    
- A **"escala" de transformação** que a matriz representa (em geometria, o determinante indica quanto a área ou volume é ampliado ou reduzido pela transformação associada à matriz).
    

Conceitualmente, o determinante é uma medida de **"não degeneração"** da matriz: se for zero, a matriz "aplana" o espaço de alguma forma e não é invertível; se for diferente de zero, a matriz preserva dimensões e é invertível.

### Inverse Matrices

<iframe width="560" height="315" src="https://www.youtube.com/embed/F10TdwBH8qc?si=5MP_t8yuz-k204m_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![[Pasted image 20251011224937.png]]

## Statistical Measures

### Covariance

It measures how two variables, x and y, change together. If the variables tend to increase or decrease simultaneously, covariance is positive. If one increases while the other decreases, covariance is negative.

#### For population

![[covariance.png]]

where 𝜇x and 𝜇y are the means of X and Y, respectively.

#### For sample size N

![[covariance_for_sample.png]]

It is used for techniques like: PCA

## Correlation Analysis

### Pearson Correlation

<iframe width="560" height="315" src="https://www.youtube.com/embed/xZ_z8KWkhXE?si=hW5L1_SWPGlqSJPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Correlation measures the strength and direction of a linear relationship between two quantitative variables. It helps you understand how changes in one variable are associated with changes in another. 

A positive correlation means that as one variable increases, the other tends to increase as well. A negative correlation means that as one variable increases, the other tends to decrease.

Let me list the main ideas:

- Correlation quantifies the degree to which two variables move together.
- The correlation coefficient ranges from -1 to 1.
- A value of 1 indicates a perfect positive linear relationship.
- A value of -1 indicates a perfect negative linear relationship.
- A value of 0 indicates no linear relationship.

#### What Is Correlation?

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

![[pearson.png]]

#### Correlation vs. covariance

Both correlation and covariance measure how two variables change together, but they are different in two things: scale and interpretability.

- **Covariance** indicates the _direction_ of a linear relationship but not its strength in a standardized way. Its value depends on the units of the variables, making it hard to compare across datasets.
    
- **Correlation** standardizes the covariance by dividing by the standard deviations of the variables, producing a unitless value between -1 and 1.

### Spearman Correlation

Spearman rank correlation assesses the strength and direction of a monotonic relationship using ranked values. It's non-parametric and works well for ordinal data or non-linear but consistent trends.

![[spearman.png]]

Where:

- di = the difference between the ranks of each observation
- n = the number of observations

## Model Evaluation

### R² (Coefficient of Determination)

<iframe width="560" height="315" src="https://www.youtube.com/embed/bMccdk8EdGo?si=HSbauDjPVS-6y7YQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Dimensionality Reduction

### PCA (Principal Component Analysis)

Principal component analysis (PCA) is a linear dimensionality reduction technique that can be used to extract information from a high-dimensional space by projecting it into a lower-dimensional sub-space. If you are familiar with the language of linear algebra, you could also say that principal component analysis is finding the [eigenvectors](https://www.datacamp.com/tutorial/eigenvectors-eigenvalues) of the covariance matrix to identify the directions of maximum variance in the data.

One important thing to note about PCA is that it is an unsupervised dimensionality reduction technique, so you can cluster similar data points based on the correlation between them without any supervision (or labels).

https://www.datacamp.com/tutorial/principal-component-analysis-in-python
