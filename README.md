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
