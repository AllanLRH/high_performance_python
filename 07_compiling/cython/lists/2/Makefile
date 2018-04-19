clean:
	rm -f -rf build
	rm -f *.so
	rm -f *.html
	rm -f *.c

build:
	python setup.py build_ext --inplace

run:
	python julia1.py

do: clean build run
