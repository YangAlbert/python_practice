import pickle

#x = [1234, '456', 'hello, python']

f = open('./pickled', 'r')

x = pickle.load(f)
print `x`

#pickle.dump(x, f)
