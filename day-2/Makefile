init:
	uv init
	uv add pytest
	rm -rf .git .gitignore

clean:
	find . -prune -type d -name "__pycache__" -delete;
	find . -name output -delete

test:
	pytest

run:
	python main-1.py 

start:
	curl https://adventofcode.com/2025/day/2/input -H "Cookie: session=${AOC_SESSION}" > input

PHONY: test
