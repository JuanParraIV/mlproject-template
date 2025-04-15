vcreate:
	conda create -p venv python=3.12 -y

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	@echo "Dependencies installed."


	



.PHONY: vcreate install
# .PHONY is used to indicate that the target does not represent a file