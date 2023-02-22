from djb2 import djb2
from avalancheTest import avalancheTest



def main():
	hashFuncs = [djb2]
	# hashFuncs = [lambda x: x*33]

	for hashFunc in hashFuncs:
		print("========== Avalanche test on '{}' ==========".format(hashFunc.__name__))
		avalancheTest(hashFunc, 100000)

main()