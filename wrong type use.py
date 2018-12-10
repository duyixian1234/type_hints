a: int = 'aaa'
b: str = 1234


def func(a: int, b: int) -> str:
    return a.upper() + b.upper()

c:int = func(1, 'aaa')