import sys

_64bit = sys.maxint == 0x7fffffffffffffff

if 0x2070000 <= sys.hexversion < 0x2080000:
    if   sys.platform == "linux2" and _64bit:
        from linux.py27_64.copengl import *
    elif sys.platform == "linux2" and not _64bit:
        from linux.py27_32.copengl import *
    elif sys.platform == "darwin":
        from macosx.py27.copengl import *
    elif sys.platform == "win32":
        from windows.py27.copengl import *
    else:
        raise RuntimeError, "unsupported platform '%s'" % sys.platform
else:
    print "error importing 'copengl' module: python version 2.7.x required. you have", sys.version
    raise ImportError

