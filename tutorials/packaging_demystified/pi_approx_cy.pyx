from math import pi

def approximate_pi(iteration_count: int) -> float:
    sign, result = 1, 0.0
    for at in range(iteration_count):
        result += sign / (2 * at + 1)
        sign *= -1
    return result * 4

__all__ = (
    "approximate_pi",
)