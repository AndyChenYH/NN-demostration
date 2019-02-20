#copyright reserved to its owner
#ABC license
#do not infringe or sell
import random
from random import randint as rd
import math
import sys

w1 = 0
w2 = 0
b = 0

print("initial:\nw1: %s, w2: %s, b: %s\n" % (w1, w2, b))

class Thing():
	def __init__(self, attribute1, attribute2, attribute3):
		self.attribute1 = attribute1
		self.attribute2 = attribute2
		#0 is male, 1 is female
		self.attribute3 = attribute3
	def __repr__(self):
		return "attribute1: %s \nattribute2: %s \nattribute3: %s\n" % (self.attribute1, self.attribute2, self.attribute3)

class Individual():
	def __init__(self, w1, w2, b):
		self.w1 = w1
		self.w2 = w2
		self.b = b
		self.pred = None
	def evaluate(self, thing):
		pred = (thing.attribute1 * self.w1) + (thing.attribute2 * self.w2) + self.b
		self.pred = sigmoid(pred)
	def __repr__(self):
		return "w1: %s\nw2: %s\nb: %s\npred: %s" % (self.w1, self.w2, self.b, self.pred)


data = [
	Thing(3,   1.5,   1),
	Thing(2,   1,     0), 
	Thing(4,   1.5,   1), 
	Thing(3,   1,     0),
	Thing(3.5,  .5,   1), 
	Thing(2,   0.5,   0),
	Thing(5.5,  1,    1),
	Thing(1,    1,    0)

]


def sigmoid(x):
	return 1 / (1 + math.e ** -(0.2 * x))

def findFittest(thing, result):
	fittest = result[0]

	for individual in result:
		if thing.attribute3 == 0:
			if individual.pred < fittest.pred:
				fittest = individual
		elif thing.attribute3 == 1:
			if individual.pred > fittest.pred:
				fittest = individual
		
	return fittest

def generation(thing, w1, w2, b):
	learning_rate = 1000 #bigger number = slower learning rate
	result = []
	for i in range(1000):
		
		new_w1 = w1 + rd(-10, 10) / learning_rate
		new_w2 = w2 + rd(-10, 10) / learning_rate
		new_b = b + rd(-10, 10) / learning_rate

		individual = Individual(new_w1, new_w2, new_b)
		individual.evaluate(thing)
		result.append(individual)
	return findFittest(thing, result), result



for iteration in range(100000):
	# thing = data[iteration % len(data)]

	thing = data[rd(0, len(data) - 1)]

	fittest, lis = generation(thing, w1, w2, b)
	w1, w2, b = (fittest.w1, fittest.w2, fittest.b)

	if iteration % 50 == 0:
		print("w1: %s, w2: %s, b: %s" % (round(w1, 3), round(w2, 3), round(b, 3)))
print()
print(round(w1, 3), round(w2, 3), round(b, 3))

while True:
	attribute1 = float(input("attribute1:\n"))
	attribute2 = float(input('attribute2:\n'))


	print('final evaluation: %s' % (sigmoid(attribute1 * w1 + attribute2 * w2 + b)))


