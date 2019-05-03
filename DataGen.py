'''
Computational Cognitive Modeling - Prof. Brenden Lake and Prof. Todd Gureckis
Final Project - "Learning Conceptual Representations in Composed Patterns"
'''

'''
Data Generation

Considering the following composed hypothesis

(h1h2)     F (1,1,h1,h2,c1,c2)
(h1h2h2)   F (1,2,h1,h2,c1,c2)
(h1h1h2)   F (2,1,h1,h2,c1,c2)
(h1h2h3)   F (1,1,F (1,1,h1,h2,c1,c2),h3,c1,c3) 
(h1h2h2h3) F (1,1,F (1,2,h1,h2,c1,c2),h3,c1,c3)

'''

import random

def Prime():
	primes = []
	for i in range(101):
		flag = True
		for j in range(2,i):
			if i%j==0:
				flag = False
		if flag:
			primes.append(i)
	return primes

def EvenOdd():
	evens = []
	odds = []
	for i in range(1,101):
		if i%2 == 0:
			evens.append(i)
		else:
			odds.append(i)
	return evens, odds

def TwoPowers():
	twopowers = []
	i=2
	while(i<100):
		powers.append(i)
		i=i*2
	return twopowers

def Interval():
	intervals = []
	for i in range(1,101):
		intervals.append(i)
	return intervals

def Data(x1,x2,x3,H):
	if x1>1:

def GenData(H):
	h_one = Data(1,1,0,H)
	h_two = Data(1,2,0,H)
	h_three = Data(2,1,0,H)
	h_four = Data(1,1,1,H)
	h_five = Data(1,2,1,H)


def main():

	primes = Prime()
	evens, odds = EvenOdd()
	two_powers, three_powers = Powers()
	intervals = Interval()

	print(primes)
	print(evens)
	print(odds)
	print(two_powers)
	print(three_powers)
	print(intervals)

	GenData([primes, evens, odds, two_powers, three_powers, intervals])


  
if __name__== "__main__":
  main()