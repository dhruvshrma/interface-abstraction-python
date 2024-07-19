from typing import Protocol, List, runtime_checkable


## The Family of all polynomials
@runtime_checkable
class Polynomial(Protocol):
    def evaluate(self, x: float) -> float: ...
    def degree(self) -> int: ...


class QuadraticPolynomial:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, x: float) -> float:
        return self.a * x ** 2 + self.b * x + self.c

    def degree(self) -> int:
        return 2


class QuinticPolynomial:
    def __init__(self, coefficients: List[float]) -> None:
        if len(coefficients) != 6:
            raise ValueError("QuinticPolynomial must have 6 coefficients")
        self.coefficients = coefficients

    def evaluate(self, x: float) -> float:
        return sum([c * x ** i for i, c in enumerate(self.coefficients)])

    def degree(self) -> int:
        return 5

## Generic root finding algorithm applicable to all polynomials
def find_root_bisection(p: Polynomial, a: float, b:float, epsilon:float = 1e-6) -> float:
    if p.evaluate(a) * p.evaluate(b) > 0:
        raise ValueError("Root not guaranteed to exist in interval")
    while b - a > epsilon:
        midpoint = (a + b) / 2
        if p.evaluate(midpoint) == 0:
            return midpoint
        if p.evaluate(a) * p.evaluate(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2

