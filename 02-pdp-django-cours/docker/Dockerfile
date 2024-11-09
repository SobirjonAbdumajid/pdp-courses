FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application files to the working directory
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt


# Define the entry point
ENTRYPOINT ["python", "app.py"]