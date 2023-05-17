all: test run

test:
	python3 -m doctest main.py

run:
	python3 main.py

clean:
	rm -rf __pycache__
