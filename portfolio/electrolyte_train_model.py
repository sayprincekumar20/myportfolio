import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib


# Load your datasets
data= pd.read_csv('C:/Users/prince_singh04/myportfolio/portfolio/electrolyte_balance_dataset.csv')

# Prepare features and labels
X = data[['Serum Sodium (mmol/L)', 'Serum Potassium (mmol/L)', 'Serum Calcium (mg/dL)', 
           'Serum Magnesium (mg/dL)', 'Bicarbonate (mmol/L)', 'Phosphorus (mg/dL)']]
y = data['Outcome']

# Scale the features

scaler= StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size= 0.2, random_state= 42)

# Train the model
model= RandomForestClassifier(n_estimators= 100, random_state= 42)
model.fit(X_train, y_train)

# Save the model and  scaler
joblib.dump(model, 'electrolyte_train_model.pkl')
joblib.dump(scaler, 'scaler.pkl')