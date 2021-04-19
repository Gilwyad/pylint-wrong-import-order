# pylint-wrong-import-order
Pylint wrong import order demonstration

## Installation
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Demonstration
Pylint shows no warnings about wrong import order in file app/feature_one/views.py :

    pylint app/feature_one/views.py

But checking with isort (which is used by Pylint) it is obvious that the order is wrong:

    isort --diff app/feature_one/views.py
