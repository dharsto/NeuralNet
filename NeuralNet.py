import numpy as np

x_all = np.array(([2, 9], [1, 5], [3, 6], [4, 4], [3, 8], [2, 7], [5, 10]), dtype=float)
y = np.array(([92], [86], [89], [90], [88], [90]), dtype=float)
x_all = x_all / np.max(x_all, axis=0)
y = y / 100

X = np.split(x_all, [6])[0]
x_predicted = np.split(x_all, [6])[1]


class neural_network(object):
    def __init__(self):
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3

        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

    def forward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        o = self.sigmoid(self.z3)
        return o

    def sigmoid(self, s):
        return 1 / (1 + np.exp(-s))

    def sigmoidPrime(self, s):
        return s * (1 - s)

    def backward(self, X, y, o):
        self.o_error = y - o
        self.o_delta = self.o_error * self.sigmoidPrime(o)
        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)

    def train(self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)

    def predict(self):
        print("predicted data based on trained weights:")
        print("input (scaled): \n" + str(x_predicted))
        print("output: \n" + str(self.forward(x_predicted)))


nn = neural_network()
for i in range(10000):
    print("input: \n" + str(X))
    print("actual output: \n" + str(y))
    print("predicted output: \n" + str(nn.forward(X)))
    print("Loss: \n" + str(np.mean(np.square(y - nn.forward(X)))))
    nn.train(X, y)

nn.predict()