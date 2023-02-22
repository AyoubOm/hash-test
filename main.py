from djb2 import djb2
from avalancheTest import avalancheTest
from jenkinsOneAtATime import oneAtATime
from constants import AVALANCHE_REPS



def main():
	# hashFuncs = [oneAtATime]
	# hashFuncs = [lambda x: x*33]
	hashFuncs = [djb2]


	for hashFunc in hashFuncs:
		print("========== Avalanche test on '{}' ==========".format(hashFunc.__name__))
		avalancheTest(hashFunc, AVALANCHE_REPS)

main()