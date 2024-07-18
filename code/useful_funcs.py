
def is_prime(n: int) -> bool:
    """Checks if the given number is prime."""
    if n == 2:
        return True
    elif n <= 1 or n % 2 == 0:
        return False

    # Start with the smallest possible divisor for odd numbers, 3.
    d = 3

    # Only check divisors less then or equal to sqrt(n). If there is a
    # divisor between sqrt(n) and n, there must be one below sqrt(n) too.
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    # If we have not found any divisors, n is prime.
    return True


def prime_generator(start = 2):
    """Generates primes, starting from k (inclusive)."""
    k = start
    if k == 2:
        yield 2
        k += 1
    elif k % 2 == 0:
        k += 1

    # We check every odd number if it is prime and if so, we yield it.
    while True:
        if is_prime(k):
            yield k
        k += 2


def get_primes_under(limit:int) -> list[int]:
    """Computes all primes lower than the limit."""
    # Create sieve where every number is marked as prime
    sieve = [1 for _ in range(limit)]

    # 0 and 1 are not prime, 2 is
    sieve[0:3] = [0, 0, 1]

    # Current prime number
    n = 2

    while n < limit:

        # Mark every multiple of n as not prime
        multiplier = 2
        while n * multiplier < limit:
            sieve[n * multiplier] = 0
            multiplier += 1
        
        # Next, not marked number is not prime. End, if we finished list
        n += 1
        while n < limit and sieve[n] == 0:
            n += 1

    return [i for i in range(limit) if sieve[i]==1]


def get_prime_divisors(numb: int) -> list:
    if numb <= 1:
        return False
    if is_prime(numb):
        return [numb]

    prime_divisors = []

    # We handle the prime divisor 2 ever now so the next code can ignore even numbers as candidates
    while numb % 2 == 0:
        prime_divisors.append(2)
        numb //= 2

    # Prime number 3 is the first candidate (we add 2 in the while loop)
    candidate = 1

    # We divide numb by its prime divisors as long as it is not 1 yet
    while numb != 1:
        # Find next prime number
        candidate += 2
        while not is_prime(candidate):
            candidate += 2

        # Divide numb by p as long as it is divisible and add every divisior to the list
        while numb % candidate == 0:
            prime_divisors.append(candidate)
            numb = numb // candidate

    return prime_divisors


def get_all_divisors(n) -> set:
    """
    We check for every number lower or equals sqrt(n) if it divides n
    or not. Bigger numbers must have a counterpart under sqrt(n). Finding
    a divisor underneath, gives us the bigger factor by computing n//i.
    """
    divisors = set()

    # Go through every number under sqrt(n) and check if it is a divisor
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.update({i, n//i})
        i += 1

    return divisors


def digital_sum(n) -> int:
    return sum(digit_list(n))


def digit_reverse(n):
    l = digit_list(n)
    k = len(l)
    # The digits are yet in the right order in the list
    # Multiply the digit with the power of ten with their
    # own index as power
    return sum( [ l[i] * 10**i for i in range(k)] )


def digit_list(n) -> list:
    l = list()

    # As long as we still have digits in n
    while n > 0:
        
        # Get the last digit
        d = n % 10

        # Add to our list
        l.insert(0, d)

        # Cut off the last digit
        n //= 10
    return l


def is_palindrome(numb):
    l = digit_list(numb)

    # Go through both sides simultaneously and check if the digits are the same
    i = 0
    j = len(l) - 1
    while i <= j:
        if l[i] != l[j]:
            return False
        i += 1
        j -= 1

    return True


def is_pandigital(numb):
    # A n-digit number is pandigital, if it make use
    # of all the digits 1 to n exactly once
    n = digit_list(numb)

    # Get the digits need to be in a n-length number (1, ..., n)
    digits = range(1, len(n)+1)

    # Check the digits
    for i in digits:
        if not i in n:
            return False
    return True
