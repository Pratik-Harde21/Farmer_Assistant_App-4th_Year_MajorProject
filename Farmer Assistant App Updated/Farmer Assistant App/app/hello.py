#prime number ?

a=2
num=13
while num > a :
  if num%a==0 & a!=num:
    print('not prime')
    break
  i += 1
else: # loop not exited via break
  print('prime')


for a in range(a, num):
    if a % num == 0:
        print('not prime')
        break
else: # loop not exited via break
    print('prime')


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))




