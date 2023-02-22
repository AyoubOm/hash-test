NB_BITS = 16
MIN_AVALANCHE = 1/3
MAX_AVALANCHE = 2/3

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def red(num):
	return f"{bcolors.FAIL}"+str(num)+f"{bcolors.ENDC}"

def green(num):
	return f"{bcolors.OKGREEN}"+str(num)+f"{bcolors.ENDC}"
