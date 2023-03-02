from constants import MASK


def fnv_1a(num: int) -> int:
	hashed = 5183
	while num > 0:
		bit = num & 8
		hashed = hashed ^ bit
		hashed = hashed * 43
		hashed = hashed & MASK
		num = num >> 8
	return hashed & MASK

