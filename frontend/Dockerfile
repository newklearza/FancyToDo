# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the application's dependencies
RUN pip install -r requirements.txt

# Expose the port your Flask app runs on (frontend runs on 80)
EXPOSE 80

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
