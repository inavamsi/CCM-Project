
import random
import numpy as np

final_seq1 = []
final_seq2 = []
final_seq3 = []

def Gen_Data(c1, p1, p2, mean, variance, ntype):
	seq = [c1]

	for i in range(5):

		#d1 = c1
		#c1 = int (round(c1 + np.random.normal(mean,variance)))

		c1 = c1 * p2 + p1
		'''if(ntype == "STAT"):
			c1 = d1 * p2 + p1
		else:
			c1 = c1 * p2 + p1'''

		if p2==3 or p2==2:
			if c1 < 1000:
				seq.append(c1)
			else:
				return False, seq 
		else:
			if c1 < 100:
				seq.append(c1)
			else:
				return False,seq

	if p2==1:
		if seq in final_seq1:
			return False, seq
		else:
			#print(seq, p1, p2)
			final_seq1.append( seq )
		return True, final_seq1

	if p2==2:
		if seq in final_seq2:
			return False, seq
		else:
			#print(seq, p1, p2)
			final_seq2.append( seq )
		return True, final_seq2

	if p2==3:
		print(seq)
		if seq in final_seq3:
			return False, seq
		else:
			#print(seq, p1, p2)
			final_seq3.append( seq )
		return True, final_seq3


def main():

	count = 0
	p2 = 1
	ntype = "STAT"
	mean = 0 
	variance = 0
	while(True):
		if p2 == 1:
			for c1 in range(1,41):
				for p1 in range(1, 11):
					if count == 200:
						p2 = 2
						break
					present, seqlist = Gen_Data(c1, p1, p2, mean, variance, ntype)
					if present :
						count += 1
						simpleh_list = seqlist

		elif p2 == 2:
			for c1 in range(1,10):
				for p1 in range(0,9):
					present, seqlist = Gen_Data(c1, p1, p2, mean, variance, ntype)
					if present :
						count += 1
						mul2_list = seqlist
			p2 = 3


		elif p2 == 3:
			for c1 in range(1,10):
				for p1 in range(0,9):
					present, seqlist = Gen_Data(c1, p1, p2, mean, variance, ntype)
					if present :
						count += 1
						mul3_list = seqlist
			break


	random.shuffle(simpleh_list)
	random.shuffle(mul2_list)
	random.shuffle(mul3_list)


	final_list = simpleh_list + mul2_list + mul3_list

	random.shuffle(final_list)

	for seq in final_list:
		print(seq)
	print(len(final_list))

  	print(len(simpleh_list))
  	print(len(mul2_list))
  	print(len(mul3_list))
if __name__== "__main__":
  main()
