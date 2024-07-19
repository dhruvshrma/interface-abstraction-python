from typing import Protocol, List, runtime_checkable
from src.protocol import protocol
from abc import ABC, abstractmethod


## The Family of all polynomials
@protocol
class Polynomial:
    def evaluate(self, x: float) -> float:
        pass

    def degree(self) -> int:
        pass

    def derivative(self) -> "Polynomial":
        pass


class PolynomialOfDegreeN(Polynomial, ABC):
    def __init__(self, coefficients: List[float]) -> None:
        self.coefficients = coefficients

    def evaluate(self, x: float) -> float:
        ## This should be in the reverse order
        return sum([c * x**i for i, c in enumerate(self.coefficients)])

    @abstractmethod
    def degree(self) -> int:
        pass

    def derivative(self) -> "Polynomial":
        new_coeffs = [i * c for i, c in enumerate(self.coefficients[1:], start=1)]
        return type(self)(new_coeffs)

    def __repr__(self):
        ## print the polynomial expansion using the coefficients
        return " + ".join([f"{c}x^{i}" for i, c in enumerate(self.coefficients)])


class QuadraticPolynomial(PolynomialOfDegreeN):
    def degree(self) -> int:
        return 2


class CubicPolynomial(PolynomialOfDegreeN):
    def degree(self) -> int:
        return 3


class QuinticPolynomial(PolynomialOfDegreeN):
    def degree(self) -> int:
        return 5


## Generic root finding algorithm applicable to all polynomials
def find_root_bisection(
    p: Polynomial, a: float, b: float, epsilon: float = 1e-6
) -> float:
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
