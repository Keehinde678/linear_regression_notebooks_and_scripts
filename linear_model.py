#!/usr/bin/env python
# coding: utf-8

# # Linear Regression in Python
# This notebook demonstrates how to perform simple linear regression using Python. It includes data visualization, model fitting, regression line overlay, and model evaluation.
# 
# BSGP 7030
# 
# **Objectives:**
# - Load and explore a CSV dataset
# - Create a scatter plot using seaborn
# - Fit a linear regression model using `sklearn`
# - Overlay the regression line on the plot
# - Evaluate the model using Mean Squared Error and R² Score

# # Import Libraries

# In[3]:


# Install seaborn if not already installed
try:
    import seaborn as sns
except ImportError:
    import sys
    get_ipython().system('{sys.executable} -m pip install seaborn')
    import seaborn as sns

# Import essential libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# # Load Dataset

# In[13]:


import pandas as pd

# Load dataset from two directories up, then into data/
df = pd.read_csv("../../data/regression_data.csv")

# Preview the data
df.head()


# # Visualize Scatter Plot

# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns

# Define columns
x_col = 'YearsExperience'
y_col = 'Salary'

# Scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(x=df[x_col], y=df[y_col])
plt.title(f"Scatter Plot of {y_col} vs {x_col}")
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.show()



# # Fit a Linear Regression Model

# In[17]:


from sklearn.linear_model import LinearRegression

# Prepare the features (X) and target (y)
X = df[[x_col]]  # 2D array for sklearn
y = df[y_col]

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict y values using the model
y_pred = model.predict(X)


# # Plot Scatter with Regression Line

# In[19]:


plt.figure(figsize=(8,6))
sns.scatterplot(x=df[x_col], y=df[y_col], label='Actual Data')

# Convert to numpy arrays for smooth plotting
plt.plot(df[x_col].to_numpy(), y_pred, color='red', label='Regression Line')

plt.title(f"Linear Regression: {y_col} vs {x_col}")
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.legend()
plt.show()



# # Evaluate the model with metrics

# In[20]:


from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")


# # Save the plot as an image file (PNG)

# In[21]:


plt.figure(figsize=(8,6))
sns.scatterplot(x=df[x_col], y=df[y_col], label='Actual Data')
plt.plot(df[x_col].to_numpy(), y_pred, color='red', label='Regression Line')
plt.title(f"Linear Regression: {y_col} vs {x_col}")
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.legend()

# Save the figure
plt.savefig('linear_regression_python_output.png', dpi=300)

plt.show()

