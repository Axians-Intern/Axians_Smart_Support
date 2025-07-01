# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Start the app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
# Note: Ensure that 'run:app' points to the correct Flask app instance in your project.
# If your Flask app is defined in a different file, adjust the CMD accordingly.
# For example, if your app is in 'app.py', use 'app:app'.
# If you have a different entry point, adjust the CMD line accordingly.
# If you need to run migrations or other setup tasks, consider adding those commands before the CMD line.
# If you have a requirements.txt file, ensure it includes all necessary dependencies.
# If you need to run any additional setup commands, you can add them before the CMD line.
# If you need to set environment variables, you can use the ENV instruction.
# If you need to run any additional setup commands, you can add them before the CMD line.