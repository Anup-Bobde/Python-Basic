# The ml file & app file should be stored in same folder
import numpy as np 	
import matplotlib.pyplot as plt
import pandas as pd	
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Load the dataset
dataset = pd.read_csv(r'C:\Users\Anup\VS Code_DataAnalytics\ML_Salary\Salary_Data.csv')

# Split the data into independent and dependent variables 
X = dataset.iloc[:, :-1].values    # YearsExperience
y = dataset.iloc[:, 1].values      # Salary
# Above or in all cases we observed all data is stored in array format


# Split the dataset into training and testing sets (80-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)  
# In above code,test_size=0.20 means 20% of the data is given or testing purpose & remaining 80% of the data is given to the training purpose
# Above the data is ramdomly saved in X_train, X_test, y_train, y_test

# Train the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict the test set(means how much will be the salary for each record in X_test)
y_pred = regressor.predict(X_test)

# comparision for y_test vs y_pred
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

# Visualize the training set
plt.scatter(X_train, y_train, color='red') # Real plot
plt.plot(X_train, regressor.predict(X_train), color='blue')  # Predicted plot
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualize the test set
plt.scatter(X_test, y_test, color='red') 
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Predict salary for 12 and 20 years of experience using the trained model
y_12 = regressor.predict([[12]])
y_20 = regressor.predict([[20]])
print(f"Predicted salary for 12 years of experience: ${y_12[0]:,.2f}")
print(f"Predicted salary for 20 years of experience: ${y_20[0]:,.2f}")
# Above is f string is used, .2f means 2 decimal after point(.)

# Check model performance
bias = regressor.score(X_train, y_train)
variance = regressor.score(X_test, y_test)
train_mse = mean_squared_error(y_train, regressor.predict(X_train))
test_mse = mean_squared_error(y_test, y_pred)

print(f"Training Score (R^2): {bias:.2f}")
print(f"Testing Score (R^2): {variance:.2f}")
print(f"Training MSE: {train_mse:.2f}")
print(f"Test MSE: {test_mse:.2f}")

# Save the trained model to disk(pickling)
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:      # Here wb means 'binary write' mode
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model.pkl")

import os 
print(os.getcwd())  # To get the location of pickle file
