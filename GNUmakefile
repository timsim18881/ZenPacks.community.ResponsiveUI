PYTHON=$(shell which python)
HERE=$(PWD)
ZP_DIR=$(HERE)/ZenPacks/community/ResponsiveUI

default: build

egg:
	python setup.py bdist_egg

build:
	python setup.py bdist_egg
	python setup.py build

clean:
	rm -rf build dist *.egg-info
