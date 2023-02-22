NB_BITS = 16
MASK = (1 << NB_BITS) - 1

STRONG_AVALANCHE = 0.1
WEAK_AVALANCHE = 1/6

AVALANCHE_REPS = 100000


class colors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    WEAK = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def bad(num):
	return f"{colors.FAIL}"+str(num)+f"{colors.ENDC}"

def strong(num):
	return f"{colors.OK}"+str(num)+f"{colors.ENDC}"

def weak(num):
	return f"{colors.WEAK}"+str(num)+f"{colors.ENDC}"
