"""
Why this test
1- allow to see quickly the result on known and my custom modified hash functions
2- Tune the constants used in famous hash functions and understand why the creator choosed them
"""
from typing import List
from random import randint
from constants import *



def avalancheTest(hashFunc: callable, nbReps: int) -> List[List[float]]:
	"""
	return avalanche matrix: input bits (rows) and output bits (cols).
	The cell value is the probability of output bit change if input bit change
	"""
	counts = [[0 for _ in range(NB_OUTPUT_BITS)] for _ in range(NB_INPUT_BITS)]

	for rep in range(nbReps):
		initialNum = rngInt()
		initialHash = hashFunc(initialNum)

		for inputBit in range(NB_INPUT_BITS):
			secondNum = flipBit(initialNum, inputBit)
			secondHash = hashFunc(secondNum)

			for outputBit in range(NB_OUTPUT_BITS):
				initialBitValue = getBit(initialHash, inputBit)
				outputBitValue = getBit(secondHash, outputBit)
				counts[inputBit][outputBit] += initialBitValue ^ outputBitValue 


	avalancheMatrix = [[(counts[inBit][outBit] / nbReps) for outBit in range(NB_OUTPUT_BITS)] for inBit in range(NB_INPUT_BITS)]
	pprintAvalanche(avalancheMatrix)
	return avalancheMatrix


def pprintAvalanche(matrix: List[List[float]]):
	"""
	pprint avalanche matrix
	"""
	for i, row in enumerate(matrix):
		print("{}".format(i + 1), end='\t')
		for col in row:
			deviation = abs(col - 0.5)

			if deviation <= STRONG_AVALANCHE:
				print(strong(col), end='\t')
			elif deviation <= WEAK_AVALANCHE:
				print(weak(col), end='\t')
			else:
				print(bad(col), end='\t')				
		print()



def rngInt():
	"""
	rng used by Avalanche test to choose a number to bit flip
	For the moment we deal only with 32bits integers
	"""
	MAX_INT = (1 << NB_INPUT_BITS) - 1
	return randint(0, MAX_INT)


def flipBit(num: int, bit: int):
	"""
	flip the bit bit in number num
	bit is 0-indexed
	"""
	return num ^ (1 << bit) if bit < NB_INPUT_BITS else num


def getBit(num: int, bit: int):
	"""
	bit is 0-indexed
	"""
	return (num >> bit) & 1

	