import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import statsmodels.api as sm

# 1. LOAD DATA
file_path = "/storage/emulated/0/Download/multi-marketing-data.csv"

df = pd.read_csv(file_path)
print(df.head())

# 2. DATA EXPLORATION AND CLEANING
print(df.info())
print(df.isnull().sum())

#Remove missing values
df = df.dropna()
print(df.shape)

# 3. DESCRIPTIVE STATISTICS

print(df.describe())

with open("Descriptive_Statistic.txt", "w") as f:
    f.write(df.describe().to_string())


#4. MULTICOLLINEARITY CHECK

print(df['TV'].unique()) # Check unique values in TV column

print(df['Influencer'].unique()) # Check unique values in Influencer column


df['TV']= df['TV'].map({'Low':1, 'High':2, 'Medium':3})

df['Influencer'] = df['Influencer'].map({'Nano':1, 'Micro':2, 'Macro':3, 'Mega':4})

X = df[['TV', 'Radio', 'Social Media', 'Influencer']]

print(X.head())
  
#  CORRELATION  CHECK

plt.figure(figsize=(8,6))

sns.heatmap(
    X.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Matrix')
plt.show()


# VIF CHECK

vif_data = pd.DataFrame()
vif_data["feature"] = X.columns

vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
print(vif_data)

with open("Multicollinearity_check.txt", "w") as f:
    f.write(vif_data.to_string())
    
#5. LINEARITY CHECK
fig, axes = plt.subplots(1,3, figsize=(15,4))

axes[0].scatter(df['TV'], df['Sales'])
axes[0].set_title('TV vs Sales')

axes[1].scatter(df['Radio'], df['Sales'])
axes[1].set_title('Radio vs Sales')

axes[2].scatter(df['Social Media'], df['Sales'])
axes[2].set_title('Social Media vs Sales')

plt.tight_layout()
plt.show()


# 6. MODEL BUILDING

X = df[['TV', 'Social Media', 'Influencer']] # After Multicollinearity check, l drop independent variable ('Radio'') since it's highly correlated to avoid redundancy 
y = df['Sales']
print(y)


# Fitting OLS Model
X = sm.add_constant(X)
ols_model = sm.OLS(y,X). fit()
print (ols_model.summary())

with open("Model_Summary.txt", "w") as f:
    f.write(ols_model.summary().as_text())


# 7. COEFFICIENT AND CONFIDENT INTERVAL


print(ols_model.params)
print(ols_model.conf_int())

with open("Confidences_Intervals.txt", "w") as f:
    f.write(ols_model.conf_int().to_string())


# 8. PREDICTION AND RESIDUAL

residuals = ols_model.resid
predicted = ols_model.fittedvalues


# 9. RESIDUALS VS FITTED
# HOMOSCEDASTICITY CHECK

plt.figure(figsize=(8,5))
plt.scatter(predicted, residuals)

plt.axhline(y=0,
            color='red',
            linestyle='--')

plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Values')

plt.show()

# 10. HISTOGRAM OF RESIDUALS
# NORMALITY CHECK



plt.figure(figsize=(8,5))

plt.hist(
    residuals,
    bins=20
)

plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Histogram of Residuals")
plt.show()


# 11. Q-Q PLOT
# NORMALITY CHECK


sm.qqplot(
    residuals,
    line='45'
)

plt.title("Q-Q Plot of Residuals")
plt.show()