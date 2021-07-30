<h1 align="center">Runtimecheck</h1>

<div align="center">

 [![PyPI version](https://badge.fury.io/py/runtimecheck.svg)](https://badge.fury.io/py/runtimecheck)
[![Downloads](https://static.pepy.tech/personalized-badge/runtimecheck?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads)](https://pepy.tech/project/runtimecheck)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://www.linkedin.com/in/eden-constantino/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rasa.svg)](https://pypi.python.org/pypi/runtimecheck)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/jusce17/runtimecheck)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>


# Runtimecheck

Originally Forked from the [Time-Logger](https://github.com/ishaansharma7/Time-Logger) Runtimecheck is an efficient Python library to help you quickly measure your functions's running time on a jupyter noetbook



## Installation

On the terminal

```bash
pip install runtimecheck
```
On a Jupyter Notebook
```bash
!pip install runtimecheck
```
## Example Usage

```python
import time

from runtimecheck.Timer import check_runtime

@check_runtime()
def hello_world():    
    time.sleep(2)
    print("Hello World")


say_hi()

```
### Result
```bash
>> Hello World
>> hello_world ran in 2.0001 seconds
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
