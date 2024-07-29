import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv('D:/Pickle/kyphosis.csv')


X = data.drop('Kyphosis', axis=1)
y = data['Kyphosis']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)


with open('trained_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully.")

print (model.predict([[24,4,10]]))