libcopengl
==========

A very limited but fast opengl wrapper for python. Wraps parts of the fixed-function pipeline.


Implementation idea:

    Use a part of glew.h (here named opengl_preprocess.h) to generate most of
    the cython opengl wrapper functions, but override some of the
    autogenerated wrappers with functions from handmadewrappers.pyx.

    Automatic generation doesn't work for functions that have pointers in
    parameters or return values.

    glew:

        The OpenGL Extension Wrangler Library
        http://glew.sourceforge.net/


Building:

    python generate_pyx.py (ignore the warnings)
    python setup.py build

    result:

      copenglconstans.py
      copengl.so
