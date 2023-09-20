install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval src/*.ipynb
	python -m pytest -vv --cov=src.lib

format:	
	black *.py
	nbqa black *.ipynb

lint:
	pylint --disable=R,C --ignore-patterns=src/*.py

run:
	nbqa ruff *.ipynb
	ruff check *.py
		
all: install lint format test 
