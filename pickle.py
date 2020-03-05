import pickle

class Veggy():
    def __init__(self):
        self.color = ''
    def set_color(self, color):
        self.color = color

cucumber = Veggy()
cucumber.set_color('green')

with open('test_pickle.pkl', 'wb') as pickle_out:
    pickle.dump(cucumber, pickle_out)

with open('test_pickle.pkl', 'rb') as pickle_in:
    unpickled_cucumber = pickle.load(pickle_in)

print(unpickled_cucumber.color)