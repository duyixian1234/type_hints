
Type Hints in Python
====================

一、基本使用
------------

.. code:: ipython3

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

**注意**\ ：只声明过类型提示的变量在没被赋值的情况下在运行时是不存在的
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    d: str
    d


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-6ce0a91deb03> in <module>
          1 d: str
    ----> 2 d
    

    NameError: name 'd' is not defined


.. code:: ipython3

    Person().name


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-3-5991b417898f> in <module>
    ----> 1 Person().name
    

    AttributeError: 'Person' object has no attribute 'name'


二、如何获得类型提示信息
------------------------

1. ``__annotations__`` 魔法方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    globals()['__annotations__']




.. parsed-literal::

    {'a': int, 'b': str, 'c': list, 'd': str}



.. code:: ipython3

    add.__annotations__




.. parsed-literal::

    {'a': int, 'b': int, 'return': int}



.. code:: ipython3

    Person.__annotations__




.. parsed-literal::

    {'name': str, 'sex': str, 'age': int}



2.\ ``inspect.signature()``\ 方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    import inspect

.. code:: ipython3

    inspect.signature(add)




.. parsed-literal::

    <Signature (a: int, b: int) -> int>



3.\ ``typing.get_type_hints()``\ 方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    from typing import get_type_hints

.. code:: ipython3

    get_type_hints(add)




.. parsed-literal::

    {'a': int, 'b': int, 'return': int}



.. code:: ipython3

    get_type_hints(Person)




.. parsed-literal::

    {'name': str, 'sex': str, 'age': int}



三、可用作类型提示的类型
------------------------

`概览 <https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html>`__

1. 基础类型

.. code:: ipython3

    a: int = 1
    b: str = 'aaa'
    c: list = [1, 2, 3]
    d: dict = {'a': 'b'}
    e: set = {1, 2, 3}
    f: tuple = (1, 2, 3)

2. typing模块， 复杂类型

.. code:: ipython3

    import typing

.. code:: ipython3

    a: typing.List[int] = [1, 2, 3]
    b: typing.Tuple[str, int, float] = ('aaa', 1, 2.5)
    c: typing.Mapping[str, int] = {'aaa': 111, 'bbb': 2}

.. code:: ipython3

    def func() -> typing.Callable[[int, int], int]:
        def add(a:int, b:int)-> int:
            return a + b

.. code:: ipython3

    a:typing.Union[int, str] = 1

.. code:: ipython3

    a:typing.Optional[str] = None

3. 使用字符串替代还未定义的类型

.. code:: ipython3

    def say(a: 'Person') -> typing.NoReturn:
        a.say_hello()
    
    class Person:
        def __init__(self, name):
            self.name = name
        def say_hello(self):
            print(f'{self.name} says:"Hello"')
    
    typing.get_type_hints(say)




.. parsed-literal::

    {'a': __main__.Person, 'return': typing.NoReturn}



4. 复杂的类型可以使用别名

.. code:: ipython3

    PersonList = typing.List[Person]
    
    def say_together(person_list: PersonList):
        for person in person_list:
            person.say_hello()
    
    typing.get_type_hints(say_together)




.. parsed-literal::

    {'person_list': typing.List[__main__.Person]}



四、类型提示的用处
------------------

1. 给人看
~~~~~~~~~

2. 静态分析 mypy
~~~~~~~~~~~~~~~~

3. 编辑器和IDE的类型推导和错误提示
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4. 一些实用场景
~~~~~~~~~~~~~~~

.. code:: ipython3

    from abc import ABCMeta, abstractmethod
    
    class Base(metaclass=ABCMeta):
        @abstractmethod
        def add(self, a:int, b:int)->int:
            ''''''
    typing.get_type_hints(Base.add)




.. parsed-literal::

    {'a': int, 'b': int, 'return': int}



.. code:: ipython3

    from functools import singledispatch
    @singledispatch
    def add(a, b):
        ''''''
    @add.register
    def add_int(a:int, b:int):
        return a + b
    add(1,2)




.. parsed-literal::

    3



.. code:: ipython3

    add('a', 'b')

.. code:: ipython3

    @add.register
    def add_str(a:str, b:str):
        return a + '_' + b
    add(1,2)
    add('a', 'b')




.. parsed-literal::

    'a_b'



在Vibora框架中的用法
~~~~~~~~~~~~~~~~~~~~

.. code:: python

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

