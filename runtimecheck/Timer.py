from functools import wraps
import os
import logging
from datetime import datetime

def check_runtime():

    def my_timer(orig_func):

        @wraps(orig_func)
        def wrapper(*args, **kwargs):

            starting_time = datetime.now()
            t1 = datetime.today().timestamp()
            result = orig_func(*args, **kwargs)
            ended_time = datetime.now()
            t2 = datetime.today().timestamp() - t1
            print(f'{orig_func.__name__} ran in {round(t2, 4)} seconds')

            return result
        return wrapper
    return my_timer
