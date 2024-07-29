import pickle

with open('aiml.pkl', 'rb') as file:
    model = pickle.load(file)
    
print (model)