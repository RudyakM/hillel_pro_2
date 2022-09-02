# Install programs and venv

## Formatters
    1. black
    2. isort 
    3. yapf
    4. PyCharm

## Linters
    1. flake8
    2. pylint

# Commands 

## venv 
    1. python3 -m venv venv
    2. virtualenv -p python3 venv 

## Activate venv for Windows
    - .\venv\Scripts\activate

## Activate venv for Linux
    - source venv/bin/activate

## pip
    1. pip install {text}
    2. pip freeze > requirements.txt
    3. pip install -r requirements.txt

# Usage
    black ./
    black --check ./

    flake8 ./

    isort ./
    isort --check-only ./