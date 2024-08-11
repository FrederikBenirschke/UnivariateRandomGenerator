import random
import math


import random
import math
import matplotlib.pyplot as plt

def uniform(a: float = 0, b: float = 1) -> float:
    """
    Generates a random number uniformly distributed between a and b. Runtime is O(1).

    Parameters:
    a (float): The lower bound of the range (inclusive). Defaults to 0.
    b (float): The upper bound of the range (exclusive). Defaults to 1.

    Returns:
    float: A random number between a and b.
    """
    return a + random.random() * (b - a)

def uniform_int(a: int, b: int) -> int:
    """
    Generates a random integer uniformly distributed between a and b (inclusive). Runtime is O(1).

    Parameters:
    a (int): The lower bound of the range (inclusive).
    b (int): The upper bound of the range (inclusive).

    Returns:
    int: A random integer between a and b (inclusive).
    """
    return math.floor(uniform(a, b + 1))

def normal(mu: float, sigma: float) -> float:
    """
    Calculates a random number following a normal distribution. Runtime is O(1).

    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.

    Returns:
    float: A random number drawn from the normal distribution with mean mu and standard deviation sigma.
    """
    r = math.sqrt(-2 * math.log(uniform()))
    x = r * math.cos(2 * math.pi * uniform())

    return mu + sigma * x

def exponential(exp_lambda: float) -> float:
    """
    Generates a random number following an exponential distribution.
    Runtime is O(1).

    Parameters:
    exp_lambda (float): The rate parameter of the exponential distribution.

    Returns:
    float: A random number drawn from the exponential distribution with rate exp_lambda.
    """
    return -1 / exp_lambda * math.log(uniform())

def poisson(exp_lambda: float) -> int:
    """
    Generates a random number following a Poisson distribution.
    Expected runtime is O(exp_lambda).

    Parameters:
    exp_lambda (float): The rate parameter of the Poisson distribution.

    Returns:
    int: A random number drawn from the Poisson distribution with rate exp_lambda.
    """
    T = 0
    counter = 0
    while T < 1:
        T += exponential(exp_lambda)
        counter += 1

    return counter

def ber(p: float) -> bool:
    """
    Generates a Bernoulli random variable. Runtime is O(1).

    Parameters:
    p (float): The probability of the Bernoulli variable being True.

    Returns:
    bool: A boolean value representing the Bernoulli random variable.
    """
    return uniform_int(0, 1) < p

def binom(n: int, p: float = 0.5) -> int:
    """
    Generates a random number following a binomial distribution. Runtime is O(n).

    Parameters:
    n (int): The number of trials in the binomial distribution.
    p (float, optional): The probability of success in each trial. Defaults to 0.5.

    Returns:
    int: A random number drawn from the binomial distribution with n trials and probability p.
    """
    return sum(ber(p) for _ in range(n))

def geom(p: float) -> int:
    """
    Generates a random number following a geometric distribution. Runtime is O(1).

    Parameters:
    p (float): The probability of success in a single trial.

    Returns:
    int: A random number drawn from the geometric distribution with success probability p.
    """
    exp_lambda = -math.log(1 - p)
    return math.floor(exponential(exp_lambda))

def chi(k: int) -> float:
    """
    Calculates the value of the chi-squared distribution. Runetime is O(k).

    Parameters:
    k (int): The number of degrees of freedom.

    Returns:
    float: The value of the chi-squared distribution.
    """

    return sum(normal(0, 1) ** 2 for _ in range(k))

def uniform_disk(r: float) -> list[float]:
    """
    Generates a random point uniformly distributed inside a disk. Runtime is O(1).

    Parameters:
    r (float): The radius of the disk.

    Returns:
    List[float]: A list containing the x and y coordinates of the generated point.
    """

    u = uniform(0, 1)
    phi = 2 * math.pi * uniform(0, 1)
    x = r * math.sqrt(u) * math.cos(phi)
    y = r * math.sqrt(u) * math.sin(phi)
    return [x, y]

def uniform_circle(r: float) -> list[float]:
    """
    Generates a random point on a circle of radius r. Runtime is O(1).

    Parameters:
    r (float): The radius of the circle.

    Returns:
    list: A list containing the x and y coordinates of the random point on the circle.
    """

    phi = 2 * math.pi * uniform(0, 1)
    u = math.sqrt(-2*math.log(uniform(0, 1)))
    x = r *  math.cos(phi)
    y = r * math.sin(phi)
    d = math.sqrt(x**2 + y**2)
    return r* [x/d, y/d]

