
c_funcs.so: c_funcs.c
	cc -fPIC -shared -o c_funcs.so c_funcs.c

clean:
	rm *.so
