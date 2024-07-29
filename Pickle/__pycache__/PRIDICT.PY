import pickle

with open ('trained_model.pkl', 'rb') as file:
    clf=pickle.load(file)
    
pridiction = clf.predict(([[24,4,10]]))
print (pridiction)