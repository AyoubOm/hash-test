"""
Why this test
1- allow to see quickly the result on known and my custom modified hash functions
2- Tune the constants used in famous hash functions and understand why the creator choosed them
"""

NB_BITS = 32


def avalancheTest(hashFunc: callable, nbReps: int) -> list<list<float>:
	"""
	return avalanche matrix: input bits (rows) and output bits (cols).
	The cell value is the probability of output bit change if input bit change
	"""
	counts = [[0 for _ in range(NB_BITS)] for _ in range(NB_BITS)]

	for rep in nbReps:
		initialNum = rngInt()
		initialHash = hashFunc(initialNum)

		for inputBit in range(NB_BITS):
			secondNum = flipBit(initialNum, inputBit)
			secondHash = hashFunc(secondNum)

			for outputBit in range(NB_BITS):
				initialBitValue = getBit(initialHash, inputBit)
				outputBitValue = getBit(secondHash, outputBit)
				counts[inputBit][outputBit] += initialBitValue ^ outputBitValue 

	return [[(counts[inBit][outBit] / nbReps) for outBit in range(NB_BITS)] for inBit in range(NB_BITS)]


def pprintAvalanche(matrix: list<list<int>):
	"""
	pprint avalanche matrix
	"""
	for i, row in enumerate(matrix):
		print("{}\t".format(i))
		for col in row:
			print(matrix[row][col], end='\t')
		print()



def rngInt():
	"""
	rng used by Avalanche test to choose a number to bit flip
	For the moment we deal only with 32bits integers
	"""
	MAX_INT = (1 << NB_BITS) - 1
	return randint(0, MAX_INT)


def flipBit(num: int, bit: int):
	"""
	flip the bit bit in number num
	bit is 0-indexed
	"""
	return num ^ (1 << bit) if bit < NB_BITS else num


def getBit(num: int, bit: int):
	"""
	bit is 0-indexed
	"""
	return (num >> bit) & 1



def main(hashFunc: callable, nbReps: int):
	matrix = avalancheTest(hashFunc, nbReps)
	pprintAvalanche(matrix)
