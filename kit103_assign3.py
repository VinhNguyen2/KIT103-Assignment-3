'''
KIT103/KMA155 Programming Assignment 3: Number Theory part 1
Submission script

Name: Vinh Nguyen
ID: 470821

Enter your answers to each question below by completing each
function. After answering a question run this script and test
your implementation in the IPython console.
'''


# Question 1: Divisibility of really, really big integers (2 marks)

def divisible_by_4(s):
    '''Returns True if the number represented by the string s is
    divisible by 4, False otherwise.'''
    return int((s[-2]+s[-1])) % 4 ==0

def divisible_by_5(s):
    '''Returns True if the number represented by the string s is
    divisible by 5, False otherwise.'''
    return int(s[-1])==5 or int(s[-1])==0

def divisible_by_9(s):
    '''Returns True if the number represented by the string s is
    divisible by 9, False otherwise.'''
    sum = 0
    for i in s:
        sum = sum + int(i)
    return sum % 9 == 0

def divisible_by_11(s):
    '''Returns True if the number represented by the string s is
    divisible by 11, False otherwise.'''
    a = 0
    b = 0
    for i in range(len(s)):
        if i % 2 == 0:
            a = a + int(s[i])
        else:
            b = b + int(s[i])   
    return (a - b) % 11 == 0


# Question 2: LCM from a prime factorisations (2 marks)

from collections import Counter

def q2_factor_lcm(a, b):
    '''Returns lcm(a, b), calculated from their prime factorisations.'''
    f_a = factor_list(a)
    f_b = factor_list(b)
    
    bag_a = Counter(f_a)
    bag_b = Counter(f_b)
    
    exps = bag_a | bag_b
    lcm = 1
    for p in exps:
        lcm = lcm*(p**exps[p])
    return lcm


# Question 3: Are a and b coprime (i.e., relatively prime)? (1 mark)

def q3_coprime(a, b):
    '''Uses the prime factorisations of a and b to determine if they are coprime.
    Returns True if they are coprime, False otherwise.
    '''
    f_a = factor_list(a)
    f_b = factor_list(b)
    
    bag_a = Counter(f_a)
    bag_b = Counter(f_b)
    
    for i in bag_a:
        for j in bag_b:
            if i == j:
                return False    
    return True


# End of answers


# Provided functions

from math import floor, sqrt

def primes(n):
    primes = set(range(2, n+1))
    for k in range(2, floor(sqrt(n))+1):
        if k in primes:
            primes.difference_update( range(k**2, n+1, k) )
    return primes

def primes_list(n):
    return sorted(primes(n))

def factor_list(n):
    factors = []
    iprimes = iter( primes_list(n) )
    while n > 1:
        p = next(iprimes)
        while n % p == 0:
            n = n // p
            factors.append(p)
    return factors

# End of provided functions
