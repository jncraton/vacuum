all: test run

test:
	python3 -m doctest main.py

media/%.svg: media/%.gv
	circo -T svg -o "$@" "$<"

run:
	python3 main.py

clean:
	rm -rf __pycache__
