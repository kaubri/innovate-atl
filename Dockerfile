# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Pass the New Relic license key as a build argument
ARG NEW_RELIC_LICENSE_KEY

# Generate New Relic config
RUN newrelic-admin generate-config $NEW_RELIC_LICENSE_KEY newrelic.ini

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable for New Relic
ENV NEW_RELIC_CONFIG_FILE=newrelic.ini

# Run newrelic-admin run-program to start the application
CMD ["newrelic-admin", "run-program", "python", "citypulse.py"]