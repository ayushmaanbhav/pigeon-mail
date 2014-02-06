from distutils.core import setup, Extension
setup(name="pigeon",version='1.0',\
	ext_modules=[Extension('pigeon',['pigeon.c'])])
