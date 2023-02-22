from constants import NB_BITS

MASK = (1 << NB_BITS) - 1


def djb2(num: int) -> int:
	hashed = 5183
	while num > 0:
		bit = num & 1
		hashed = (hashed << 5) + hashed + bit
		hashed = hashed & MASK
		num = num >> 1
	return hashed & MASK
