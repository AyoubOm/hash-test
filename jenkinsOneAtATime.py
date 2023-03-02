from constants import MASK



def oneAtATime(num: int) -> int:
  hashed = 0
  while num > 0:
    octet = num & ((1 << 8) - 1)
    hashed += octet
    hashed += hashed << 10
    hashed ^= hashed >> 6
    hashed = hashed & MASK

    num = num >> 8

  hashed += hashed << 3
  hashed ^= hashed >> 11
  hashed += hashed << 15
  return hashed & MASK
