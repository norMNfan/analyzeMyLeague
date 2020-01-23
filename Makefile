HOST=127.0.0.1
PORT=9000

init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test