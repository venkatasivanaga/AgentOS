.PHONY: setup update run clean test

# Create virtual environment and install all dependencies
setup:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	@echo "Setup complete. Run 'source venv/bin/activate' to activate."

# Save your current dependencies to requirements.txt
update:
	./venv/bin/pip freeze > requirements.txt
	@echo "requirements.txt updated."

# Run the main application
run:
	PYTHONPATH=. ./venv/bin/python backend/main.py

# Destroy all temporary environments and cache files for a fresh start
clean:
	rm -rf venv node_modules dist build __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "Repository cleaned."