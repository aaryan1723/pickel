import pickle

with open('aiml.pkl', 'rb') as file:
    name = pickle.load(file)
    
new_name = "krutin"
name.append(new_name)

with open ('aiml.pkl','wb') as file:
    pickle.dump(name,file)