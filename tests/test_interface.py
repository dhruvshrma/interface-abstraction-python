from src.polynomial import (
    Polynomial,
    QuadraticPolynomial,
    QuinticPolynomial,
    find_root_bisection,
)
from typing import Protocol
from src.protocol import protocol


@protocol
class EmptySubProtocol:
    def evaluate(self, x: float) -> float:
        pass  # type: ignore

    def degree(self) -> int:
        pass  # type: ignore


class EmptySubProtocol2:
    def evaluate(self, x: float) -> float:
        pass  # type: ignore

    def degree(self) -> int:
        pass  # type: ignore


def test_protocol_is_implemented():
    quad = QuadraticPolynomial([1, 2, 3])
    assert isinstance(quad, Polynomial)
    assert isinstance(QuinticPolynomial([1, 2, 3, 4, 5, 6]), Polynomial)


def test_subprotocol():
    class EmptySubProtocol(Polynomial):
        def evaluate(self, x: float) -> float: ...

        def degree(self) -> int: ...

    assert isinstance(EmptySubProtocol(), Polynomial)


def test_root_finding_works():
    quad = QuadraticPolynomial([-4, 0, 1])
    # use repr to print the polynomial
    # assert repr(quad) == "1x^0 + 0x^1 + -4x^2"
    root = find_root_bisection(quad, 1, 4)
    print(quad)
    assert abs(root - 2) < 1e-6


def test_protocol_decorator():
    # check that it is of type Protocol
    assert issubclass(EmptySubProtocol, Protocol)
    assert not issubclass(EmptySubProtocol2, Protocol)

def test_derivative_is_polynomial():
    quad = QuadraticPolynomial([1, 2, 3])
    assert isinstance(quad.derivative(), Polynomial)
    assert isinstance(quad.derivative(), QuadraticPolynomial)
