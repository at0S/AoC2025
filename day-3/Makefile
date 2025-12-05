init:
	uv init
	uv add pytest
	rm -rf .git .gitignore

	mv main.py main-1.py
	cp main-1.py main-2.py

clean:
	find . -prune -type d -name "__pycache__" -delete;
	find . -name output -delete

test:
	pytest

run-%:
	uv run main-$*.py 

start-%:
	curl https://adventofcode.com/2025/day/$*/input -H "Cookie: session=${AOC_SESSION}" > input

PHONY: test
