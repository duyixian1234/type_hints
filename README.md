# 介绍Python 3.5+ 版本的新语言特性；Type Hints
## 项目内容
### `type hints.ipynb`
本地有Python 3.7版本的jupyter环境的同学可以启动jupyter-notebook查看notebook，或者使用pipenv创建新的虚拟环境。
不想创建虚拟环境的同学可以在[nbviewer](https://nbviewer.jupyter.org/github/duyixian1234/type_hints/blob/master/type%20hints.ipynb)网站上查看notebook。
### `wrong type use.py`
不遵从类型提示的代码，可以正确运行，但在mypy等静态分析工具下会报错。可以直接在命令行下运行`mypy wrong\ type\ use.py`,或者在VS Code的设置中配置`"python.linting.mypyEnabled": true`。
### `autocomplete.py`
演示编辑器和IDE可以识别定义了类型提示的变量并进行自动补全。