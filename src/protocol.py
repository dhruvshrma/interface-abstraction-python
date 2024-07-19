from typing import Protocol, TypeVar, cast, get_type_hints, runtime_checkable, Callable

T = TypeVar("T")

## Decorator to transform a class into a protocol
def protocol(cls:T) -> T:
    annotations = get_type_hints(cls)
    methods = {name: value for name, value in cls.__dict__.items() if callable(value) and not name.startswith("__")}

    @runtime_checkable
    class ProtocolClass(Protocol):
        pass

    for name, method in methods.items():
        if method.__code__.co_code == b'd\x00S\x00':
            setattr(ProtocolClass, name, cast(object, ...))
        else:
            setattr(ProtocolClass, name, method)

    for name, typ in annotations.items():
        if name not in methods:
            setattr(ProtocolClass, name, cast(object, ...))

    ProtocolClass.__name__ = cls.__name__  # type: ignore
    ProtocolClass.__qualname__ = cls.__qualname__  # type: ignore
    ProtocolClass.__module__ = cls.__module__
    ProtocolClass.__annotations__ = annotations

    return cast(T, ProtocolClass)