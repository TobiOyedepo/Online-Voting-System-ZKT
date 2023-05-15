import random

def zkp(p,g):
    # Define the group parameters
    p = 17
    g = 3
    # Generate a random secret value
    x = random.randint(1, p-1)
    # Compute the public key
    y = pow(g, x, p)
    # Generate a random challenge
    c = random.randint(0, 1)

    # Compute the response
    r = (x + c) % (p-1)

    # Verify the proof
    if pow(g, r, p) == (y * pow(y, c, p)) % p:
        return 1
    else:
        return 0
