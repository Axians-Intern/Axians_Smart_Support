from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
# This will run the Flask application when this script is executed directly.
# Make sure to set the environment variable FLASK_APP to this file or run it with python run.py.
# You can also set the debug mode by setting the environment variable FLASK_DEBUG to 1.
# For example, you can run the app with:
# ```bash       
# export FLASK_APP=run.py
# export FLASK_DEBUG=1
# python run.py
# ```
# Or simply run:
# ```bash
# python run.py
# ```
# if you have the Flask app configured to run in debug mode by default. 
# This will start the Flask development server, and you can access the app at http://localhost:5000 by default.
# Make sure to have the necessary dependencies installed, such as Flask, LangChain, and any other required libraries.
# You can install them using pip:
# ```bash   
# pip install flask langchain
# ```
# Ensure you have the correct versions of the libraries as per your requirements.
# If you are using a virtual environment, make sure to activate it before running the app.
# You can also run the app in production mode using a WSGI server like Gunicorn
# or uWSGI, but for development purposes, the built-in Flask server is sufficient.
# If you want to run the app in a Docker container, you can create a Dockerfile
# and build the image, then run the container with the necessary environment variables set.
# Here's a simple Dockerfile example:
# ```dockerfile
# FROM python:3.9-slim
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE 5000
# CMD ["python", "run.py"]
# ```
# You can build the Docker image with:
# ```bash
# docker build -t my_flask_app .
# ```
# And run the container with:
# ```bash
# docker run -p 5000:5000 my_flask_app
# ```
# This will expose the Flask app on port 5000 of your host machine.
# Make sure to adjust the Dockerfile and commands according to your project structure and requirements.
# You can also use Docker Compose for more complex setups with multiple services.
# Here's a simple docker-compose.yml example:
# ```yaml
# version: '3.8'
# services:
#   web:
#     build: .
#     ports:
#       - "5000:5000"
#     environment:
#       - FLASK_APP=run.py
#       - FLASK_DEBUG=1
#     volumes:
#       - .:/app
# ```
# You can run the app with Docker Compose using:
# ```bash
# docker-compose up
# ```
# This will build the image and start the Flask app in a container, making it accessible at
# http://localhost:5000.
# Make sure to adjust the Dockerfile and docker-compose.yml according to your project structure and requirements.
# You can also add more services, such as a database or a cache, to the Docker
# Compose file if needed.
# This will help you to run your Flask application in a containerized environment,
# making it easier to manage dependencies and configurations.
# Remember to keep your code organized and modular, separating concerns into different files and directories.
# This will make it easier to maintain and scale your application in the future.
# You can also consider using a configuration management tool like Flask-Config or Flask-Env
# to manage different configurations for development, testing, and production environments.
# This will help you to keep your code clean and avoid hardcoding sensitive information like API keys
# or database credentials in your source code.
# Instead, you can use environment variables or configuration files to manage these settings securely.
# Additionally, consider implementing logging and error handling to monitor your application
# and handle exceptions gracefully. You can use Flask's built-in logging or integrate with a logging
# service like Sentry or Loggly for better visibility into your application's performance and issues.
# Finally, make sure to test your application thoroughly before deploying it to production.
# You can use Flask's testing framework or third-party libraries like pytest to write unit tests and
# integration tests for your application. This will help you to catch bugs early and ensure that your
# application behaves as expected under different scenarios.
# You can also consider setting up a continuous integration/continuous deployment (CI/CD) pipeline
# to automate the testing and deployment process, ensuring that your application is always in a deployable
# state and reducing the risk of human error during deployments.
# This can be done using tools like GitHub Actions, Travis CI, or CircleCI,
# which can run your tests and deploy your application automatically whenever you push changes to your repository.
# By following these best practices, you can build a robust and maintainable Flask application
# that is easy to deploy and scale as your user base grows.
# Remember to keep your dependencies up to date and monitor your application's performance
# to ensure that it remains responsive and reliable over time.