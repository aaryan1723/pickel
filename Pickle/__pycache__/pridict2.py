import pickle

with open ('trained_model.pkl', 'rb') as file:
    clf=pickle.load(file)
    
pridiction = clf.predict(([[71,3,5,2,2,0]]))
print (pridiction)