import pickle

f = open("test.pck", "w")

pickle.dump(12.3, f)
pickle.dump([1, 2, 3], f)

f.close()

f = open("test.pck", "r")
x = pickle.load(f)
print x 
print type(x)
x = pickle.load(f)
print x
print type(x)