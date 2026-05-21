.PHONY: setup test run clean

setup:
python -m venv venv
./venv/bin/pip install -r requirements.txt
npm install

test:
./venv/bin/pytest tests/
npm test

run:
docker-compose up --build

clean:
rm -rf venv node_modules dist __pycache__ .pytest_cache
