
# Type Hints in Python
## 一、基本使用


```python
a:int = 1
b:str = 'aaa'
c:list
c = [1, 2, 3]

def add(a:int, b:int)->int:
    return a + b

class Person:
    name:str
    sex:str = 'Male'
    age:int
```


### **注意**：只声明过类型提示的变量在没被赋值的情况下在运行时是不存在的


```python
d: str
d
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-6ce0a91deb03> in <module>
          1 d: str
    ----> 2 d
    

    NameError: name 'd' is not defined



```python
Person().name
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-3-5991b417898f> in <module>
    ----> 1 Person().name
    

    AttributeError: 'Person' object has no attribute 'name'


## 二、如何获得类型提示信息
### 1. `__annotations__` 魔法方法


```python
globals()['__annotations__']
```




    {'a': int, 'b': str, 'c': list, 'd': str}




```python
add.__annotations__
```




    {'a': int, 'b': int, 'return': int}




```python
Person.__annotations__
```




    {'name': str, 'sex': str, 'age': int}



### 2.`inspect.signature()`方法


```python
import inspect
```


```python
inspect.signature(add)
```




    <Signature (a: int, b: int) -> int>



### 3.`typing.get_type_hints()`方法


```python
from typing import get_type_hints
```


```python
get_type_hints(add)
```




    {'a': int, 'b': int, 'return': int}




```python
get_type_hints(Person)
```




    {'name': str, 'sex': str, 'age': int}



## 三、可用作类型提示的类型
[概览](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

1. 基础类型


```python
a: int = 1
b: str = 'aaa'
c: list = [1, 2, 3]
d: dict = {'a': 'b'}
e: set = {1, 2, 3}
f: tuple = (1, 2, 3)
```

2. typing模块， 复杂类型


```python
import typing
```


```python
a: typing.List[int] = [1, 2, 3]
b: typing.Tuple[str, int, float] = ('aaa', 1, 2.5)
c: typing.Mapping[str, int] = {'aaa': 111, 'bbb': 2}
```


```python
def func() -> typing.Callable[[int, int], int]:
    def add(a:int, b:int)-> int:
        return a + b
```


```python
a:typing.Union[int, str] = 1
```


```python
a:typing.Optional[str] = None
```

3. 使用字符串替代还未定义的类型


```python
def say(a: 'Person') -> typing.NoReturn:
    a.say_hello()

class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f'{self.name} says:"Hello"')

typing.get_type_hints(say)
```




    {'a': __main__.Person, 'return': typing.NoReturn}



4. 复杂的类型可以使用别名


```python
PersonList = typing.List[Person]

def say_together(person_list: PersonList):
    for person in person_list:
        person.say_hello()

typing.get_type_hints(say_together)
```




    {'person_list': typing.List[__main__.Person]}



## 四、类型提示的用处
### 1. 给人看
### 2. 静态分析 mypy
### 3. 编辑器和IDE的类型推导和错误提示
### 4. 一些实用场景


```python
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def add(self, a:int, b:int)->int:
        ''''''
typing.get_type_hints(Base.add)
```




    {'a': int, 'b': int, 'return': int}




```python
from functools import singledispatch
@singledispatch
def add(a, b):
    ''''''
@add.register
def add_int(a:int, b:int):
    return a + b
add(1,2)
```




    3




```python
add('a', 'b')
```


```python
@add.register
def add_str(a:str, b:str):
    return a + '_' + b
add(1,2)
add('a', 'b')
```




    'a_b'



### 在Vibora框架中的用法
```python
from vibora import Vibora, Request
from vibora.responses import JsonResponse
​
app = Vibora()
​
@app.route('/')
async def home(request: Request):
    values = await request.json()
    print(values)
    return JsonResponse(values)
​
app.run()
```


```python

```
