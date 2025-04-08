from math import gcd
from random import randint

# Point addition on elliptic curve modulo N
def add_points(P, Q, a, N):
    if P == Q:
        numerator = 3 * P[0] ** 2 + a
        denominator = 2 * P[1]
    else:
        numerator = Q[1] - P[1]
        denominator = Q[0] - P[0]

    try:
        inv = pow(denominator, -1, N)
    except ValueError:
        factor = gcd(denominator, N)
        if 1 < factor < N:
            raise Exception(f"Factor found: {factor}")
        else:
            raise Exception("Failed inverse with no factor")

    m = (numerator * inv) % N
    x_r = (m ** 2 - P[0] - Q[0]) % N
    y_r = (m * (P[0] - x_r) - P[1]) % N
    return (x_r, y_r)

# ECM with multiple retries for reliability
def ECM(N, retries=10, max_steps=50):
    for attempt in range(retries):
        a = randint(1, N - 1)
        x = randint(1, N - 1)
        y = randint(1, N - 1)
        P = (x, y)
        try:
            for _ in range(max_steps):
                P = add_points(P, P, a, N)
        except Exception as e:
            if "Factor found" in str(e):
                factor = int(str(e).split(":")[-1].strip())
                return factor
    return None  # Failed after all retries

# Test on a small composite number
N = 77  # 7 * 11
factor = ECM(N)

if factor:
    print(f"\n Non-trivial factor of {N} is: {factor}")
else:
    print(f"\n Failed to find factor of {N} after retries.")



