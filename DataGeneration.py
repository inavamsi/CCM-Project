'''
Computational Cognitive Modeling - Prof. Brenden Lake and Prof. Todd Gureckis
Final Project - "Sequence Prediction using Bayesian Concept Learning"
'''

'''
Data Generation:

Guassian Noise: Mean =  0 | Variance = 0.66

Files To Be Generated:-

	1.  Stationary_Noise_80_19_1
	2.  Stationary_Noise_40_40_20
	3.  Stationary_Noise_34_33_33

	4.  Progessive_Noise_80_19_1
	5.  Progessive_Noise_40_40_10
	6.  Progessive_Noise_34_33_33

'''

import numpy as np 
import random
import math


def GenSequencesProgressive(hypothesis, mean, variance, sequence_count):

	sequence_list = []
	count = 0
	while True:
		flag = True
		if count == sequence_count:
			break
		if (hypothesis == "+"):
			val = np.random.normal(mean, variance)
			val = int(np.sign(val) * math.floor(abs(val)))
			start = random.randint(1, 41) + val
			temp = start 
			sequence = [temp]
			factor = [ random.choice([i for i in range(1,11)]) ]
			for i in range(5):
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				if i >= 3:
					temp = temp + factor[0] 
				else:
					temp = temp + factor[0] + val
				sequence.append(temp)

		elif (hypothesis == 'x'):
			factor = [random.choice([2,3])]

			if (factor[0] == 2):
				start = random.randint(1,10)
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				start = start + val
				if start <= 0:
					continue

			if (factor[0] == 3):
				start = random.randint(1,4)
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				start = start + val
				if start <= 0:
					continue
			temp = start
			sequence = [temp]
			for i in range(5):
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				if i >=3:
					temp = temp * factor[0]
				else:
					temp = temp * factor[0] + val

				if temp <= 0 :#or temp > 500:
					flag = False
					break
				sequence.append(temp)

		elif (hypothesis == "x+"):
			factor = [random.choice([2,3]), 0]
			if factor[0] == 2:
				factor[1] = random.choice([i for i in range(1,11)])
			if factor[0] == 3:
				factor[1] = random.choice([i for i in range(1,6)])

			if (factor[0] == 2):
				start = random.randint(1,7)
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				start = start + val
				if start <= 0:
					continue

			if (factor[0] == 3):
				start = random.randint(1,2)
				if start <= 0:
					continue

			temp = start
			sequence = [temp]
			for i in range(5):
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				if (factor[0]==3):
					if i >=3 or i==0:
						temp = temp * factor[0] + factor[1]
					else:
						temp = temp * factor[0] + factor[1] + val
				else:
					if i >=3 or i==0:
						temp = temp * factor[0] + factor[1]
					else:
						temp = temp * factor[0] + factor[1] + val

				if temp <= 0 :#or temp > 500:
					flag = False
					break
				sequence.append(temp)


		if (not (sequence in sequence_list) and flag):
			sequence_list.append(sequence)
			count += 1

	return sequence_list

def GenSequencesStationary(hypothesis, mean, variance, sequence_count):

	sequence_list = []
	count = 0
	while True:
		flag = True
		if count == sequence_count:
			break
		if (hypothesis == "+"):
			val = np.random.normal(mean, variance)
			val = int(np.sign(val) * math.floor(abs(val)))
			start = random.randint(1, 41)
			temp_actual = start 
			temp = start + val
			sequence = [temp]
			factor = [ random.choice([i for i in range(1,11)]) ]
			for i in range(5):
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				if i>=3:
					temp = temp_actual + factor[0]
				else:
					temp = temp_actual + factor[0] + val
				temp_actual = temp_actual + factor[0]
				sequence.append(temp)

		elif (hypothesis == 'x'):
			factor = [random.choice([2,3])]

			if (factor[0] == 2):
				start = random.randint(1,10)
				temp_actual = start
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				start = start + val
				if start <= 0:
					continue

			if (factor[0] == 3):
				start = random.randint(1,4)
				temp_actual = start
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				start = start + val
				if start <= 0:
					continue
			temp = start
			sequence = [temp]
			for i in range(5):
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				if i>=3:
					temp = temp_actual * factor[0] 
				else:
					temp = temp_actual * factor[0] + val
				temp_actual = temp_actual * factor[0]
				if temp <= 0 :#or temp > 500:
					flag = False
					break
				sequence.append(temp)

		elif (hypothesis == "x+"):
			factor = [random.choice([2,3]),0]
			if factor[0] == 2:
				factor[1] = random.choice([i for i in range(1,11)])
			if factor[0] == 3:
				factor[1] = random.choice([i for i in range(1,6)])

			if (factor[0] == 2):
				start = random.randint(1,7)
				temp_actual = start
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
				start = start + val
				if start <= 0:
					continue

			if (factor[0] == 3):
				start = random.randint(1,2)
				temp_actual = start
				if start <= 0:
					continue

			temp = start
			sequence = [temp]
			for i in range(5):
				val = np.random.normal(mean, variance)
				val = int(np.sign(val) * math.floor(abs(val)))
		
				if i >=3:
					temp = temp_actual * factor[0] + factor[1]
				else:
					temp = temp_actual * factor[0] + factor[1] + val

				temp_actual = temp_actual * factor[0] + factor[1]
				if temp <= 0 :#or temp > 500:
					flag = False
					break
				sequence.append(temp)


		if (not (sequence in sequence_list) and flag):
			sequence_list.append(sequence)
			count += 1

	return sequence_list



def GenNoiseStationary(mean, variance, hypothesis, sequence_count):

	if (hypothesis == "+"):
		return GenSequencesStationary(hypothesis, mean, variance, sequence_count)

	if (hypothesis == "x"):
		return GenSequencesStationary(hypothesis, mean, variance, sequence_count)

	if (hypothesis == "x+"):
		return GenSequencesStationary(hypothesis, mean, variance, sequence_count)

def GenNoiseProgressive(mean, variance, hypothesis, sequence_count):

	if (hypothesis == "+"):
		return GenSequencesProgressive(hypothesis, mean, variance, sequence_count)

	if (hypothesis == "x"):
		return GenSequencesProgressive(hypothesis, mean, variance, sequence_count)

	if (hypothesis == "x+"):
		return GenSequencesProgressive(hypothesis, mean, variance, sequence_count)


def PrintSequences(L):
	for l in L:
		print(l)

def WriteFile(filename, L):
	with open(filename, "w") as f:
		for s in L:
			f.write(str(s) +"\n")

def main():

	mean = 0
	variance = 0.66

	x = 600
	y = 300
	z = 200
	Addition_Hypotheses_Stationary = GenNoiseStationary(0,0.66,"+",x)
	Multiplication_Hypotheses_Stationary = GenNoiseStationary(0,0.66,"x",z)

	Addition_Hypotheses_Progressive = GenNoiseProgressive(0,0.66,"+",x)
	Multiplication_Hypotheses_Progressive = GenNoiseProgressive(0,0.66,"x",y)

	Comb_Hypotheses_Stationary = GenNoiseStationary(0,0.66,"x+",z)
	Comb_Hypotheses_Progressive = GenNoiseProgressive(0,0.66,"x+",y)

	WriteFile("Addition_Hypotheses_Stationary.txt", Addition_Hypotheses_Stationary)
	WriteFile("Addition_Hypotheses_Progressive.txt", Addition_Hypotheses_Progressive)

	WriteFile("Multiplication_Hypotheses_Stationary.txt", Multiplication_Hypotheses_Stationary)
	WriteFile("Multiplication_Hypotheses_Progressive.txt", Multiplication_Hypotheses_Progressive)

	WriteFile("Comb_Hypotheses_Stationary.txt", Comb_Hypotheses_Stationary)
	WriteFile("Comb_Hypotheses_Progressive.txt", Comb_Hypotheses_Progressive)
	
	'''print("Addition_Hypotheses_Stationary")

	PrintSequences(Addition_Hypotheses_Stationary)

	print("Multiplication_Hypotheses_Stationary")

	PrintSequences(Multiplication_Hypotheses_Stationary)

	#print("Addition_Hypotheses_Progressive")

	PrintSequences(Addition_Hypotheses_Progressive)

	print("Multiplication_Hypotheses_Progressive")

	PrintSequences(Multiplication_Hypotheses_Progressive)
	
	print("Comb_Hypotheses_Stationary")

	PrintSequences(Comb_Hypotheses_Stationary)

	#print("Comb_Hypotheses_Progressive")

	#PrintSequences(Comb_Hypotheses_Progressive)

	print(len(Comb_Hypotheses_Stationary))
	print(len(Comb_Hypotheses_Progressive))'''

if __name__== "__main__":
  main()