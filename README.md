Minimal project to showcase how to call C functions from Python (Tested on Python 3.6).


* The C functions are defined in `c_funcs.c`.

* The `Makefile` compiles the C source code into dynamic library files (`c_funcs.so`).


* `funcs.py` imports the C library code using CDLL and wraps them in new Python functions.

  You would send this function to your users (to be used as a Python library).


* `example_usage.py` uses the functions (re-)defined in `funcs.py`.

  The end-user would write the code in `example_usage.py`.
