import pickle

with open("test1.pkl", "rd") as f:
    result = pickle.load(f)
    print(result)
