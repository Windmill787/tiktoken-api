.PHONY: install run start stop

# Define the Flask application file
APP_FILE = app.py

# Define the process name to be used for finding and stopping the application
PROCESS_NAME = "python $(APP_FILE)"

install:
	@echo "Installing Python dependencies..."
	@pip install -r requirements.txt

run:
	@echo "Starting Flask application..."
	@python $(APP_FILE)

start:
	@echo "Starting Flask application with nohup..."
	@nohup python $(APP_FILE) &

stop:
	@echo "Stopping Flask application..."
	@pkill -f $(PROCESS_NAME)
