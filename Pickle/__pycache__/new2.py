import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
new_data = pd.read_csv('D:\Pickle\data.csv')

X_new = new_data.drop('Review', axis=1)
y_new = new_data['Review']

old_data = pd.read_csv('D:/Pickle/kyphosis.csv')
X_old = old_data.drop('Kyphosis', axis=1)
y_old = old_data['Kyphosis']


X_combined = pd.concat([X_old, X_new])
y_combined = pd.concat([y_old, y_new])


X_train, X_test, y_train, y_test = train_test_split(X_combined, y_combined, test_size=0.2, random_state=42)


model.fit(X_train, y_train)


with open('trained_model.pkl', 'wb') as file:
    pickle.dump(model, file)