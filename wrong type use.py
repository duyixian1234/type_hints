import typing
a: int = 'aaa'
b: str = 1234


def func(a: int, b: int) -> str:
    return a.upper() + b.upper()

c:int = func(1, 'aaa')

d:typing.Tuple[int, str, float] = (1, 1, 1)