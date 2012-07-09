import random
from config import *

seq = [x for x in URLS for y in range(URLS[x])]

counts = {}

for i in range(0, 1000):
	choice = random.choice(seq)
	if choice in counts:
			counts[choice] += 1
	else:
			counts[choice] = 1

print counts
