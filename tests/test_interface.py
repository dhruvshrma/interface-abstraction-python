from src.polynomial import Polynomial, QuadraticPolynomial, QuinticPolynomial, find_root_bisection


def test_protocol_is_implemented():
    assert isinstance(QuadraticPolynomial(1, 2, 3), Polynomial)
    assert isinstance(QuinticPolynomial([1, 2, 3, 4, 5, 6]), Polynomial)


def test_subprotocol():
    class EmptySubProtocol(Polynomial):
        def evaluate(self, x: float) -> float: ...

        def degree(self) -> int: ...

    assert isinstance(EmptySubProtocol(), Polynomial)


def test_root_finding_works():
    quad = QuadraticPolynomial(1, 0, -4)
    root = find_root_bisection(quad, 1, 4)
    assert abs(root - 2) < 1e-6
