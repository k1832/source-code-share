import sys
def add_next_digit(threshold):
    minimum = current * 10
    for n in range(minimum, minimum+10):
        if n**2 > threshold: return n-1
    return minimum+9
def is_prime(num):
    if num == 2: return True
    if num%2 == 0 or num <= 1: return False
    i = 3
    while i*i <= num:
        if num % i == 0: return False
        i += 2
    return True

current = 1
digits = 1
while digits < 12:
    current = add_next_digit(2*(10**(2*digits)))
    digits += 1
while True:
    s = str(current)[-11:]
    if s[0] != '0' and is_prime(int(s)):
        print(current)
        print(s)
        sys.exit(0)
    current = add_next_digit(2*(10**(2*digits)))
    digits += 1