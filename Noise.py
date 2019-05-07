import numpy as np
import math

p = [2, 4, 6, 8]
count = 0
tot = 300
freq = {}
for j in range(tot):

	l = [2, 4, 6, 8]
	for i in range(len(l)):
		val = np.random.normal(0,0.6)
		if val > 0:
			val = math.floor(abs(val))
		else:
			val = -1 * math.floor(abs(val))
		l [i] += val

	for k in range(len(l)):
		if p[k] != l[k]:
			count += 1
	
	if count in freq:
		freq[count] = freq[count] + 1
	else:
		freq[count] = 1
	count = 0

print(freq)

