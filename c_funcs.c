#include <stdio.h>
// Compile with `cc -fPIC -shared -o c_funcs.so c_funcs.c`

int square(int i) {
    return i * i;
}
